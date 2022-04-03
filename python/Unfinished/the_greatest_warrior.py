class Warrior:
  def __init__(self):
    self.experience = 100
    self.achievements = []
    self.calculate_experience()

  def calculate_experience(self):
    if self.experience >= 100:
      self.level = int(self.experience//100)
    else:
      self.level = 1
    self.calculate_rank()

  def calculate_rank(self):
    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    if self.level < 1:
      self.rank = ranks[0]
    if self.level <= 100:
      self.rank = ranks[self.level//10]

  def battle(self, level):
    self.calculate_experience()
    # invalid level
    if level < 1 or level > 100:
      return "Invalid level"
    if level == self.level:
      self.experience += 10
      self.calculate_experience()
    if level == self.level-1:
      self.experience += 5
      self.calculate_experience()
    if level//10 > self.level//10 and level > self.level+5:
      return "You've been defeated"
    if level > self.level:
      self.experience += 20 * ((level-self.level)**2)
    if self.level >= level+2:
      return "Easy fight"
    if self.level >= level:
      return "A good fight"
    if self.level < level:
      return "An intense fight"

  def training(self, list):
    self.calculate_experience()
    desc, experience, min = list[0], list[1], list[2]
    if self.level >= min:
      self.achievements.append(desc)
      self.experience += experience
      self.calculate_experience()
      return desc
    else:
      return "Not strong enough"

bruce_lee = Warrior()
print(bruce_lee.level)         # => 1
print(bruce_lee.experience)   # => 100
print(bruce_lee.rank)        # => "Pushover"
print(bruce_lee.achievements)  # => []
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1])) # => "Defeated Chuck Norris"
print(bruce_lee.experience)    # => 9100
print(bruce_lee.level)       # => 91
print(bruce_lee.rank )         # => "Master"
print(bruce_lee.battle(90))  # => "A good fight"
print(bruce_lee.experience)   # => 9105
print(bruce_lee.achievements) 