import random

def genQuest():
  titles = ["Archduke",  "Assistant", "Queen", "Captain", "Jr.", "Sir","Lord", "Baron", "Farmer", "Archmage", "Supreme Lord of most of existence", "First Sea Lord", "King"]
  names = [
    "Joesephina",  "Bob", "Mary",  "Smith", "Nodrick", "Rick", "Fredrick", "Veznan", "KazaaakplethKilik", "Steve", "Asmoranomardicadaistinaculdacar", "Wolfeschlegelsteinhausenbergerdorff", "Will", "Percival", "Wolfric", "Matt", "Emmett", "Conor", "Jack", "Charlie", "Peng", "Lin", "Poe", "Steelmore", "Rolison", "Ramridder"] 
  
  quests = [
    #Quest formating should be "verb" + "explains problem"
    " tells you that a dragon is attacking the city. To save the city you need to the following: ",
    " yells at you that there is a murder in the town hall. To help police the city you need to: ",
    " told you that barbarians have entered the city. To prevent the downfall of the city you need to: ",
    " explains that the people are rising up against the taxing duke. You need to: ",
    " says the shield system for the city has been critically damaged. You need to: ",
    " sends a letter saying that Steve is burning the city down with a flint and steel. To stop this you need to:"
  ]

  objective = [
    "Fetch 3 fish from the Bay of Lakes.",
    "Kill God. (If you can't do that, do the next best thing).",
    "Clear their basement of mice.",
    "Repair their weapons systems, to ensure victory against the Flagship.",
    "Tell the Contessa that she is urgently needed to block an assasin that may or may not exist.",
    "Go kill the king of Westford.",
    "Hunt down and kill the rogue archmage fleeing through the forests to the south.",
    "Climb to the top of Frozen Peak, in order to unlock the Ice Wizard.",
    "Go mine diamonds until you have full gold armor.", 
    "Kill 39.87 goblins.",
    "Go kill an adult black dragon.",
    "Kill 14.63 kobolds."
  ]

  rewards = [ 
    "After completing, you recieve a wanted notice along with 200 gold coins for your dubious activities.",
    "After completing, you become famous through the wanted list. Many known criminals decide to help you with money and hiding. (Gain 2000 gp, but now have to hide your identity.)",
    "Completing the quest will grant you the gratitude of the quest giver, as well as the promise of hospitality should you ever come back.",
    "After completion, you have recieved a Spellguard Shield and 5 electrum pieces. ",
    "After completing the quest and/or dying, you will be awarded a posthumous medal.",
    "After finishing, you recieve a contract for your head, but get 2000 gp. ",
    "Upon completion, you find yourself shunned by the populace, but manage to steal 1000 gold pieces on your way out of town.",
    "After completing your task, the church declares holy war on you. You earn 500 gp and 1000 ep from an enemy of the church. ",
  ]

  randTitle = random.choice(titles)
  randName = random.choice(names)
  randQuests = random.choice(quests)
  randObj = random.choice(objective)
  randRew = random.choice(rewards)

  return randTitle + " " + randName + " " + randQuests + " " + randObj + " " + randRew
