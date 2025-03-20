from typing import Dict

from DataTypes import *

TROOP_LEVEL_BONUS_PERCENTAGE = 1.5

# Tribes
ROMANS = "Romans"
GAULS = "Gauls"
TEUTONS = "Teutons"

# Romans
LEGIONNAIRE = "Legionnaire"
PRAETORIAN = "Praetorian"
IMPERIAN = "Imperian"
EQUITES_LEGATI = "Equites Legati"
EQUITES_IMPERATORIS = "Equites Imperatoris"
EQUITES_CAESARIS = "Equites Caesaris"
ROMAN_RAM = "Roman Ram"
FIRE_CATAPULT = "Fire Catapult"
ROMAN_SETTLER = "Roman Settler"
SENATOR = "Senator"

# Gauls
PHALANX = "Phalanx"
SWORDSMAN = "Swordsman"
PATHFINDER = "Pathfinder"
THEUTATES_THUNDER = "Theutates Thunder"
DRUIDRIDER = "Druidrider"
HAEDUAN = "Haeduan"
GAUL_RAM = "Gaul Ram"
TREBUCHET = "Trebuchet"
GAUL_SETTLER = "Gaul Settler"
CHIEFTAIN = "Chieftain"

# Teutons
CLUBSWINGER = "Clubswinger"
SPEARMAN = "Spearman"
AXEMAN = "Axeman"
SCOUT = "Scout"
PALADIN = "Paladin"
TEUTONIC_KNIGHT = "Teutonic Knight"
TEUTON_RAM = "Teuton Ram"
CATAPULT = "Catapult"
TEUTON_SETTLER = "Teuton Settler"
CHIEF = "Chief"

TROOP_STATS: Dict[str, FightStats] = {
    LEGIONNAIRE: FightStats(35, 50, 40, 1),
    PRAETORIAN: FightStats(65, 35, 30, 1),
    IMPERIAN: FightStats(40, 25, 70, 1),
    EQUITES_LEGATI: FightStats(20, 10, 0, 2),
    EQUITES_IMPERATORIS: FightStats(65, 50, 120, 3),
    EQUITES_CAESARIS: FightStats(80, 105, 180, 4),
    ROMAN_RAM: FightStats(30, 75, 60, 3),
    FIRE_CATAPULT: FightStats(60, 10, 75, 6),
    ROMAN_SETTLER: FightStats(80, 80, 0, 1),
    SENATOR: FightStats(40, 30, 50, 5),
    
    PHALANX: FightStats(40, 50, 15, 1),
    SWORDSMAN: FightStats(35, 20, 65, 1),
    PATHFINDER: FightStats(20, 10, 0, 2),
    THEUTATES_THUNDER: FightStats(25, 40, 100, 2),
    DRUIDRIDER: FightStats(115, 55, 45, 2),
    HAEDUAN: FightStats(60, 165, 140, 3),
    GAUL_RAM: FightStats(30, 105, 50, 3),
    TREBUCHET: FightStats(45, 10, 70, 6),
    GAUL_SETTLER: FightStats(80, 80, 0, 1),
    CHIEFTAIN: FightStats(50, 50, 40, 4),
    
    CLUBSWINGER: FightStats(20, 5, 40, 1),
    SPEARMAN: FightStats(35, 60, 10, 1),
    AXEMAN: FightStats(30, 30, 60, 1),
    SCOUT: FightStats(10, 5, 0, 1),
    PALADIN: FightStats(100, 40, 55, 2),
    TEUTONIC_KNIGHT: FightStats(50, 75, 150, 3),
    TEUTON_RAM: FightStats(30, 80, 65, 3),
    CATAPULT: FightStats(60, 10, 50, 6),
    TEUTON_SETTLER: FightStats(80, 80, 10, 1),
    CHIEF: FightStats(60, 40, 40, 4),
}


ROMANS_WALL_DEFENSE_BONUS_PERCENTAGE = {
    1: 3, 2: 6, 3: 9, 4: 13, 5: 16, 6: 19, 7: 23, 8: 27, 9: 30, 10: 34,
    11: 38, 12: 43, 13: 47, 14: 51, 15: 56, 16: 60, 17: 65, 18: 70, 19: 75, 20: 81
}

GAUL_WALL_DEFENSE_BONUS_PERCENTAGE = {
    1: 3, 2: 5, 3: 8, 4: 10, 5: 13, 6: 16, 7: 19, 8: 22, 9: 25, 10: 28,
    11: 31, 12: 34, 13: 38, 14: 41, 15: 45, 16: 48, 17: 52, 18: 56, 19: 60, 20: 64
}

TEUTON_WALL_DEFENSE_BONUS_PERCENTAGE = {
    1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 13, 7: 15, 8: 17, 9: 20, 10: 22,
    11: 24, 12: 27, 13: 29, 14: 32, 15: 35, 16: 37, 17: 40, 18: 43, 19: 46, 20: 49
}