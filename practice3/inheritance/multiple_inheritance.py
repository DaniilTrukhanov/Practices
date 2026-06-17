class Kingdom:
  def __init__(self, kingdom):
    self.kingdom = "Animals"

class Family(Kingdom):
  def __init__(self, kingdom):
    super().__init__(kingdom)
    self.family = "Felines"

class Species(Family):
  def __init__(self, kingdom, family):
    super().__init__(kingdom, family)
    self.species = "Cat"