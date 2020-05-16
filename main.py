import random as rnd

class bioma:
  name = "bioma"
  def __init__(self):
    self.name = rnd.choice(["planice", "montanha"])

class loot

class block:
  biome = ''
  exits = 0b0000   # Bitflag: N S E W
  contents = []

  def __init__(self):
    self.biome = bioma()

