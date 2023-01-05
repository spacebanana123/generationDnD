import random
classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Paladin", "Rogue", "Ranger", "Sorcerer", "Warlock", "Wizard"]

races = {
    # Str, Dex, Con, Int, Wis, Cha 
    "Dragonborn":[2,0,0,0,0,1], 
    "Dwarven": [0,0,2,0,0,0], 
    "Elven": [0,2,0,0,0,0],
    "Gnomish": [0,0,0,2,0,0],
    "Half Elf": [0,0,0,1,1,2],
    "Halfling": [0,2,0,0,0,0],
    "Half Orc": [2,0,1,0,0,0],
    "Human": [1,1,1,1,1,1],
    "Tiefling": [0,0,0,1,0,2],
    "Leonin": [1,0,2,0,0,0],
    "Owlin": [0,0,0,0,0,0],
    "Aarakocra": [0,0,0,0,0,0],
    "Aasimar": [0,0,0,0,0,0],
    "Air Genasi": [0,0,0,0,0,0],
    "Bugbear": [0,0,0,0,0,0],
    "Centaur": [0,0,0,0,0,0],
    "Changeling": [0,0,0,0,0,0],
    "Deep Gnome": [0,0,0,0,0,0],
    "Duergar": [0,0,0,0,0,0],
    "Earth Genasi": [0,0,0,0,0,0],
    "Eladrin": [0,0,0,0,0,0],
    "Fairy": [0,0,0,0,0,0],
    "Firbolg": [0,0,0,0,0,0],
    "Fire Genasi": [0,0,0,0,0,0],
    "Githyanki": [0,0,0,0,0,0],
    "Githzerai": [0,0,0,0,0,0],
    "Goblin": [0,0,0,0,0,0],
    "Goliath": [0,0,0,0,0,0],
    "Harengon": [0,0,0,0,0,0],
    "Hobgoblin": [0,0,0,0,0,0],
    "Kenku": [0,0,0,0,0,0],
    "Kobold": [0,0,0,0,0,0],
    "Lizardfolk": [0,0,0,0,0,0],
    "Minotaur": [0,0,0,0,0,0],
    "Orc": [0,0,0,0,0,0],
    "Satyr": [0,0,0,0,0,0],
    "Sea Elf": [0,0,0,0,0,0],
    "Shadar Kai": [0,0,0,0,0,0],
    "Shifter": [0,0,0,0,0,0],
    "Tabaxi": [0,0,0,0,0,0],
    "Tortle": [0,0,0,0,0,0],
    "Triton": [0,0,0,0,0,0],
    "Water Genasi": [0,0,0,0,0,0],
    "Yuan Ti": [0,0,0,0,0,0],
    "Feral Tiefling": [2,0,0,1,0,0],
    "Kalashtar": [0,0,0,0,2,1],
    "Warforged": [0,0,2,1,0,0],
    "Loxodon": [0,0,2,0,1,0],
    "Simic Hybrid": [0,0,2,0,0,1],
    "Vedalken": [0,0,0,2,1,0],
    "Verdan": [0,0,1,0,0,2],
    "Locathah": [2,1,0,0,0,0],
    "Grung": [0,2,1,0,0,0],
}

def rollChar():
  classChoice = random.choice(classes)
  race, bonus = random.choice(list(races.items()))
  stats = []
  for i in range(6):
    dices = []
    for i in range(4):
      dice = random.randint(1,6)
      dices.append(dice)
    dices.remove(min(dices))
    val = 0
    for i in dices:
      val += i
    stats.append(val)

  finalStats = []
  for i in range(len(stats)):
    stat = stats[i] + bonus[i]
    finalStats.append(stat)

  con = finalStats[3]
  con -= 10
  con = con / 2
  con = round(con)
  
  if classChoice == "Wizard" or classChoice == "Sorcerer":
    health = 6 + con
  elif classChoice == "Barbarian":
    health = 12 + con
  elif classChoice == "Paladin" or classChoice == "Ranger" or classChoice == "Fighter":
    health = 10 + con
  else:
    health = 8 + con
  
  out = race + " " + classChoice + " "
  for i in finalStats:
    out += str(i)
    out += " "
  out += " with " + str(health) + " health."
  return out
  