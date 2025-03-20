from dataclasses import dataclass
from typing import List

@dataclass
class TroopInfo:
    type: str
    amount: int
    level: int

@dataclass
class TroopList:
    list: List[TroopInfo]

@dataclass
class FightStats:
    infantry_defense_points: float
    cavalry_defense_points: float
    offense_points: float
    upkeep: int

@dataclass
class VillageAlianceBonuses:
    wall_defence_bonus_percentage: int
    palace_residence_defence_bonus_points: int
    brewery_offense_bonus_percentage: int
    metalurgie_bonus_percentage: int

@dataclass
class HeroWeaponStats:
    troop_type: str
    bonus: int

@dataclass
class HeroStats:
    strength: int
    offense_bonus_percentage: float
    defense_bonus_percentage: float
    weapon: HeroWeaponStats

