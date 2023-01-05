import random
def genEnc():
  easy_num = random.randint(2, 6)
  medium_num = random.randint(3, 8)
  hard_num = random.randint(6, 12)
  
  other_encounters = [
    "An old woman is sitting on her porch, watching the players as they pass by her home. She asks the players if they have seen her lost pony. She has not lost a pony. She sells extremely rare weapons for thousands of gold pieces (the exact number of which you may decide) but only if they appear to be good people. (The woman has a set of +3 PLATE, a CLOAK OF INVISIBILITY, and an IOUN STONE OF MASTERY). ",
    "The players encounter a man who has been attacked by a pack of wolves that has mauled him terribly, leaving him for dead on the road. He will die if not rescued quickly. He is a famed blacksmith and will forge one +2 MELEE WEAPON for the party. ",
    "The party encounters a caravan of traders, who are more than happy to trade. They will trade any armor and/or weapons, acting as a normal shop. Additionally, they will also sell ARMOR OF VULNERABILITY, for a surprisingly low price of 30 gold pieces. (The armor is cursed, see description). "
  ]
  easy_encounters = [
    "The party sees a farm 300 feet down the road, there is smoke rising from the field. If the party investigates, they will find " + str(easy_num) + " GOBLINS ransacking the farm. Looting the remains of the farm will yield " + str(easy_num) + " gold pieces. "
    "As the party passes a bend in the surrounding forest, they find a hungry OWLBEAR, which immediately begins its hunt. (There are OWLBEAR footprints leading to a lair containing pelts and hides worth " + str(easy_num) + " gold pieces. ",
    "The party is attacked by a small party of " + str(easy_num + 2) + " BANDITS, although they attempt to run away as soon as they take any real losses (2 or 3 people). "
  ]
  medium_encounters = [
    "An Aurora is lost from the higher planes. It will attack any with an NEUTRAL EVIL, CHAOTIC EVIL, or LAWFUL EVIL alignments. If the players kill the Aurora, they recieve a STAFF OF HEALING. Note: The Aurora is homebrew and can be found at https://www.dandwiki.com/wiki/Aurora_(5e_Creature) ",
    "The party sees two small gray wolves in the middle of the road, howling at the moon. They are actually WEREWOLVES in wolf form, and they will attack if they sense that anyone has sympathetic magic (healing magic, bard music, etc.). ",
    "A group of " + str(medium_num) + " BANDITS is attacking a merchant caravan. If the players help the merchant caravan, they will receive a reward, depending on what the merchant is carrying. "
  ]
  hard_encounters = [
    "The party sees a group of ten CULTISTS wearing robes and carrying staffs. They are chanting a spell, and are trying to conjure a BALOR. The party can stop them, or let them summon the demon and see what happens. Looting the bodies will yield " + str(hard_num) + " gold pieces. ", 
    "An ARCHMAGE is travelling with the party. They stop for the night and hear chanting from the woods. The ARCHMAGE has snuck away from the party and has begun summoning a BEHOLDER. Upon seeing the party, the ARCHMAGE attacks. After 2 turns, the BEHOLDER will be summoned even if the ARCHMAGE has perished. The ARCHMAGE'S body contains a sizeable fortune of " + str(hard_num) + " gold pieces and a STAFF OF POWER. ",
    "The ground shakes around the adventures, and before they know it, they find themselves victims of a TARRASQUE attack. (Good luck surviving this one!) If you survive, you will rewarded with a scale of the TARRASQUE which is worth 5000 gold pieces if sold to the right merchant. ",
    "The party passes an old man on the road. He cries out for help, claiming a great evil has slaughtered his entire village. This great evil is a DEMILICH and an army of " + str(hard_num) + " SKELETONS, the DEMILICH resides inside a lair with a DEATH SLAAD, guarding a pile of 1500 gold pieces and a ELDRITCH STAFF. ",
    "Legends say there lies a sprawling cave system under <Insert Place Here> and that terrible evil lurks underneath. If the party pursues these rumors, This will end your campaign, so use our random campaign generator. The party will enter the cave system full of undead mobs of various difficulty, (perhaps add a DEMILICH miniboss) the final boss is an ANCIENT BLUE DRACOLICH, with two DEATH SLAADS acting as bodyguards. Upon slaying the ANCIENT BLUE DRACOLICH, the party will recieve the BLACKSTAFF, and the LUCK BLADE.", 
  ]
  

  other = random.choice(other_encounters)
  easy = random.choice(easy_encounters)
  med = random.choice(medium_encounters)
  hard = random.choice(hard_encounters)
  return other, easy, med, hard

def randEnc():
  things = [" Goblins ", " Kobolds ", " Red Dragon Wrymlings ", " Drow Warriors ", " Ancient Blue Dragons ", " Ogres ", " Yuan Ti Shamen ", " Commoners ", " Pirate Captains "]
  verbs = ["living in", "raiding", "running away from", "taxing", "murdering a man in", "making a fire in", "robbing a trader in"]
  places = [" Frozen Peak.", " Greenvale.", " Wilmette.", " the forest.", " a cottage.", " a farm.", " an abandonded village."]

  number = random.randint(5,39)
  thing = random.choice(things)
  verb = random.choice(verbs)
  place = random.choice(places)
  encounter = str(number) + thing + verb + place
  return encounter