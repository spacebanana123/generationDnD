import random
from dndEncouter import genEnc,randEnc
from dndQuest import genQuest

def chooseRest():
  rand = random.randint(1,3)
  if rand == 1:
    return " Immediately, "
  if rand == 2:
    return " After 3-4 hours (short rest), "
  if rand == 3:
    return " After a good nights sleep (long rest), "

def makeCampaign():
  other1, easy1, med1, hard1 = genEnc()
  other2, easy2, med2, hard2 = genEnc()
  other3, easy3, med3, hard3 = genEnc()
  quest1 = genQuest()
  quest2 = genQuest()
  quest3 = genQuest()
  
  return quest1 + chooseRest() + easy1 + chooseRest() + randEnc() + chooseRest() + med1 + "\n" + "\n" + chooseRest() + other1 + quest2 + chooseRest() + easy3 + chooseRest() + randEnc() + chooseRest() + hard1 + chooseRest() + "\n" + "\n" + other2 + quest3 + chooseRest() + randEnc() + chooseRest() + "\n" + "\n" + other3 + hard2 + "After a good nights sleep (long rest), " + hard3
