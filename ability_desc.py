## Pyromancer Descriptions:
def fire_desc():
  FIREBALL_DESC = "Fire Ball - Shoots a fireball at your enemies dealing 0.50x your damage to inital target."
  FLAMETHROWER_DESC = "Flame Thrower - Release fire from your palms dealing 0.75x your damage to your eney."
  FIRE_STORM_DESC = "Fire Storm - A hellish tornado ignites under the enemies feet dealing 1x your damge to all enemies on the field."
  fire_desc_list = [FIREBALL_DESC, FLAMETHROWER_DESC, FIRE_STORM_DESC]
  return fire_desc_list

## Cryomancer Descriptions:
def ice_desc():
  ICEBOLT_DESC = "Ice Bolt - Shoots an icicle lance at your enemies dealing 0.50x your damage to a single target of your choosing. Freezes that enemy for the entirety of their next turn."
  ICEWALL_DESC = "Ice Wall - Erect an ice wall out the ground shielding you from the next attack towards you. When broken, this wall breaks into shards which hurts the enemy that broke it for 0.75x your damage."
  BLIZZARD_DESC = "Blizzard - Conjure a blizzard that whips around snow and hail dealing 1.0x of your damage to all enemies on the field. This will freeze all enemies on the field"
  ice_desc_list = [ICEBOLT_DESC, ICEWALL_DESC, BLIZZARD_DESC]
  return ice_desc_list

## Geomancer Descriptions:
def earth_desc():
  ROCK_GAUNTLETS_DESC = "Rock Gauntlets - Encase your fist in stone punching the enemy of your choice for 0.50x your damage "
  BOULDER_THROW_DESC = "Boulder Throw - Pull a boulder out of the ground lifting it above your head and lob it at the enemy dealing 0.75x of your damage to a single target"
  EARTHQUAKE_DESC = "Earth Quake - The earth rumbles as the ground quakes summon an earth quake below your enemies dealing 1.0x of your damage to the entire field"
  earth_desc_list = [ROCK_GAUNTLETS_DESC, BOULDER_THROW_DESC, EARTHQUAKE_DESC]
  return earth_desc_list

def lightning_desc():
  ZAP_DESC = "Zap - Quickly Zap your enemies dealing 0.50x of your damage. High speed will make this ability does large amounts of damage."
  STORM_DESC = "Storm - Summon Lightning bolts from the sky dealing 0.75x damage to all enemies on the field"
  CHAIN_LIGHTNING_DESC = "Chain Lightning - Turn yourself into lightning itself Blitzing through all enemies on the field dealing 1.0x of your damage."
  lightning_desc_list = [ZAP_DESC, STORM_DESC, CHAIN_LIGHTNING_DESC]
  return lightning_desc_list