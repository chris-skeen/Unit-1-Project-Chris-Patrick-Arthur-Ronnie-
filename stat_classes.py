from dataclasses import dataclass
# MAGE CLASSES --
@dataclass
class Fire():
  original_health = 70
  health = 70
  damage = 8
  charge = 0
  turn : bool
  potion = 1
  ability1 = "Fire Ball"
  ability2 = "Flamethrower"
  ability3 = "Fire Storm"
  status = "burn"
  mage_name = "Pyromancer"

@dataclass
class Ice():

  original_health = 80
  health = 80
  damage = 6
  charge = 0
  potion = 1
  turn : bool
  ability1 = "Ice Bolt"
  ability2 = "Ice Wall"
  ability3 = "Blizzard"
  status = "ice"
  mage_name = "Cryomancer"

@dataclass
class Lightning():
  original_health = 50
  health = 50
  damage = 10
  charge = 3
  potion = 1
  turn : bool
  ability1 = "Zap"
  ability2 = "Storm"
  ability3 = "Chain Lightning"
  mage_name = "Electromancer"

@dataclass
class Earth():
  original_health = 135
  health = 135
  damage = 4
  charge = 0
  potion = 1
  turn : bool
  ability1 = "Rock Gauntlets"
  ability2 = "Boulder Throw"
  ability3 = "Earth Quake"
  mage_name = "Geomancer"
