from TravianCalculator import TravianCalculator
from Constants import *

# # Tribes
# ROMANS 
# GAULS
# TEUTONS

# # Romans
# LEGIONNAIRE
# PRAETORIAN 
# IMPERIAN
# EQUITES_LEGATI
# EQUITES_IMPERATORIS
# EQUITES_CAESARIS
# ROMAN_RAM
# FIRE_CATAPULT
# ROMAN_SETTLER
# SENATOR

# # Gauls
# PHALANX
# SWORDSMAN
# PATHFINDER
# THEUTATES_THUNDER
# DRUIDRIDER
# HAEDUAN
# GAUL_RAM
# TREBUCHET
# GAUL_SETTLER
# CHIEFTAIN

# # Teutons
# CLUBSWINGER
# SPEARMAN
# AXEMAN
# SCOUT
# PALADIN
# TEUTONIC_KNIGHT
# TEUTON_RAM
# CATAPULT
# TEUTON_SETTLER 
# CHIEF

if __name__ == '__main__':
    troops = TroopList(
        [
            TroopInfo(LEGIONNAIRE, 5000, 20),
            TroopInfo(PRAETORIAN, 5500, 20),
            TroopInfo(EQUITES_LEGATI, 189, 0),
            TroopInfo(EQUITES_IMPERATORIS, 110, 3),
            TroopInfo(EQUITES_CAESARIS, 820, 20),
            TroopInfo(FIRE_CATAPULT, 20, 0),
            TroopInfo(SENATOR, 3, 0),
        ]
    )

    hero = HeroStats(
        5000,
        3.2,
        7.8,
        HeroWeaponStats(
            EQUITES_CAESARIS,
            16
        )
    )

    tribe = TEUTONS
    wall_level = 20
    palace_residence_level = 20
    metalurgie_precentage = 6
    brewery = 20

    travian = TravianCalculator(troops, tribe, wall_level, hero, palace_residence_level, metalurgie_precentage, brewery)
    travian.calculate_stats_points()