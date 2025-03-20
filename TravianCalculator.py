import numpy as np

from DataTypes import *
from Constants import *

from typing import Optional
from tabulate import tabulate

class TravianCalculator:
    def __init__(self, troops: TroopList, tribe: str, wall_level: int, hero: Optional[HeroStats], palace_residence_level: int, metalurgie_bonus_percentage: int, brewery_level: int = 0) -> None:
        self.troops: TroopList = troops
        self.tribe: Optional[str] = None
        self.villageAlianceBonuses: VillageAlianceBonuses = VillageAlianceBonuses(0, 0, 0, 0)

        self.calculated_fight_data = []
        self.calculated_village_data = []
        
        self.set_tribe(tribe)
        self.set_wall_defense_bonus_percentage(wall_level)
        self.set_palace_residence_percentages(palace_residence_level)
        self.set_brewery_bonus_percentage(brewery_level)
        self.set_metalurgie_bonus_percentage(metalurgie_bonus_percentage)

        if hero:
            if hero.weapon:
                self.hero: HeroStats = HeroStats(hero.strength, 0, 0, hero.weapon)
                self.set_hero_bonus_percentages(hero.offense_bonus_percentage, hero.defense_bonus_percentage)
            else:
                self.hero: HeroStats = HeroStats(hero.strength, 0, 0, HeroWeaponStats("", 0))
                self.set_hero_bonus_percentages(hero.offense_bonus_percentage, hero.defense_bonus_percentage)
        else:
            self.hero: HeroStats = HeroStats(0, 0, 0, HeroWeaponStats("", 0))

    def set_tribe(self, tribe: str) -> None:
        if tribe in [ROMANS, GAULS, TEUTONS]:
            self.tribe = tribe
        else:
            raise ValueError(f"Unknown tribe: [{tribe}]")
        
    def set_wall_defense_bonus_percentage(self, wall_level: int) -> None:
        if not self.tribe:
            raise Exception(f"Wall defense bonus cannot be set. Please call 'set_tribe()' before this function.")
        
        if wall_level < 0 or wall_level > 20:
            raise ValueError(f"Wall level can be only from 0 - 20.")
        
        if self.tribe in ROMANS:
            self.villageAlianceBonuses.wall_defence_bonus_percentage = ROMANS_WALL_DEFENSE_BONUS_PERCENTAGE.get(wall_level, 0)
        elif self.tribe in GAULS:
            self.villageAlianceBonuses.wall_defence_bonus_percentage = GAUL_WALL_DEFENSE_BONUS_PERCENTAGE.get(wall_level, 0)
        elif self.tribe in TEUTONS:
            self.villageAlianceBonuses.wall_defence_bonus_percentage = TEUTON_WALL_DEFENSE_BONUS_PERCENTAGE.get(wall_level, 0)
        else:
            raise ValueError(f"Unknown tribe: [{self.tribe}]")
        
    def set_hero_bonus_percentages(self, offense_percentage: float, defense_percentage: float) -> None:
        if offense_percentage < 0 or offense_percentage > 20:
            raise ValueError(f"Hero offense bonus percentage can have values from 0 - 20.")
        
        if defense_percentage < 0 or defense_percentage > 20:
            raise ValueError(f"Hero defense bonus percentage can have values from 0 - 20.")
        
        self.hero.offense_bonus_percentage = offense_percentage
        self.hero.defense_bonus_percentage = defense_percentage

    def set_palace_residence_percentages(self, palace_residence_level: int):
        if palace_residence_level < 0 or palace_residence_level > 20:
            raise ValueError(f"Palace/Residence level can be only from 0 - 20.")
        
        self.villageAlianceBonuses.palace_residence_defence_bonus_points = 2 * (palace_residence_level * palace_residence_level)

    def set_metalurgie_bonus_percentage(self, metalurgie_bonus_percentage):
        if metalurgie_bonus_percentage not in [0, 2 ,4, 6, 8, 10]:
            raise ValueError(f"Metalurgie bonus can be only from 0, 2, 4, 6, 8, 10.")
        
        self.villageAlianceBonuses.metalurgie_bonus_percentage = metalurgie_bonus_percentage

    def set_brewery_bonus_percentage(self, brewery_level):
        if brewery_level < 0 or brewery_level > 20:
            raise ValueError(f"Brewery level can be only from 0 - 20.")
        
        self.villageAlianceBonuses.palace_residence_defence_bonus_points = brewery_level

    def calculate_smithy_level(self, base_value: int, level: int):
        # return base_value + (base_value + (300 * upkeep / 7)) * (np.power(1.007, level) - 1)
        return base_value * np.power(1.015, level)

    def add_troop_bonus(self, troop: str, level: int) -> FightStats:
        base_troop_stats: FightStats = TROOP_STATS.get(troop, FightStats(0,0,0,0))

        if troop in [SENATOR, CHIEFTAIN, CHIEF, ROMAN_SETTLER, GAUL_SETTLER, TEUTON_SETTLER]:
            self.calculated_fight_data.append([troop, 
                                           int(base_troop_stats.offense_points),
                                           int(base_troop_stats.infantry_defense_points), 
                                           int(base_troop_stats.cavalry_defense_points), 
                                           ])
            
            return TROOP_STATS.get(troop, FightStats(0,0,0,0))
        
        metalurgie_bonus = 1 + (self.villageAlianceBonuses.metalurgie_bonus_percentage / 100)
        wall_bonus = 1 + (self.villageAlianceBonuses.wall_defence_bonus_percentage / 100)
        hero_def_bonus = 1 + (self.hero.defense_bonus_percentage / 100)
        hero_off_bonus = 1 + (self.hero.offense_bonus_percentage / 100)
        brewery_bonus = 1 + (self.villageAlianceBonuses.brewery_offense_bonus_percentage / 100)

        real_troop_stats = FightStats(
            self.calculate_smithy_level(base_troop_stats.infantry_defense_points, level) * metalurgie_bonus * wall_bonus * hero_def_bonus,
            self.calculate_smithy_level(base_troop_stats.cavalry_defense_points, level) * metalurgie_bonus * wall_bonus * hero_def_bonus,
            self.calculate_smithy_level(base_troop_stats.offense_points, level) * metalurgie_bonus * hero_off_bonus * brewery_bonus,
            base_troop_stats.upkeep
        )

        if troop in self.hero.weapon.troop_type:
            real_troop_stats.infantry_defense_points += self.hero.weapon.bonus
            real_troop_stats.cavalry_defense_points += self.hero.weapon.bonus
            real_troop_stats.offense_points += self.hero.weapon.bonus

        self.calculated_fight_data.append([troop, 
                                           int(real_troop_stats.offense_points),
                                           int(real_troop_stats.infantry_defense_points), 
                                           int(real_troop_stats.cavalry_defense_points), 
                                           ])

        return real_troop_stats
    
    def calculate_stats_points(self):
        troop_stats = {}
        for troop_type in self.troops.list:
            troop_stats[troop_type.type] = {"fight_points": self.add_troop_bonus(troop_type.type, troop_type.level), "amount": troop_type.amount}

        village_stat_points = FightStats(
            self.villageAlianceBonuses.palace_residence_defence_bonus_points + self.hero.strength, 
            self.villageAlianceBonuses.palace_residence_defence_bonus_points + self.hero.strength, 
            self.hero.strength,
            0
        )

        for troop_type, troop_info in troop_stats.items():
            village_stat_points.infantry_defense_points += troop_info["fight_points"].infantry_defense_points * troop_info["amount"]
            village_stat_points.cavalry_defense_points += troop_info["fight_points"].cavalry_defense_points * troop_info["amount"]
            village_stat_points.offense_points += troop_info["fight_points"].offense_points * troop_info["amount"]


        self.calculated_village_data.append([
            "Total Village Data",
            int(village_stat_points.offense_points),
            int(village_stat_points.infantry_defense_points),
            int(village_stat_points.cavalry_defense_points)
        ])

        print(tabulate(self.calculated_fight_data, headers=["Troop", "Offense", "Infantry Defense", "Cavalry Defense"], tablefmt="grid"))
        print(tabulate(self.calculated_village_data, headers=["", "Offense", "Infantry Defense", "Cavalry Defense"], tablefmt="grid"))




        
        
