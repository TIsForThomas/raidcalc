from raid_values import *
from entity_health import *
<<<<<<< HEAD

#Getting input from user

User_wants = input("What kind of item are you looking to break: ")
if User_wants = garageDoor Print yea
User_how_many = input ("How many of this item do you need to break: ")
User_raid_type = input ("What are you going to be raiding with: ")





=======
import math
selectedEntity = input("Please select the the number that corresponds to the entity you are trying to break: 1=Wood Door, 2=Metal Door, 3=Garage Door, 4=Armored Door ")
global newSelectedEntity
global entityType
if selectedEntity == "1":
    print("You selected: Wood Door")
    newSelectedEntity = woodDoor
    entityType = "Wood Door"
elif selectedEntity == "2":
    print("You selected: Metal Door")
    newSelectedEntity = metalDoor
    entityType = "Metal Door"
elif selectedEntity == "3":
    print("You selected: Garage Door")
    newSelectedEntity = garageDoor
    entityType = "Garage Door"
elif selectedEntity == "4":
    print("You selected: Armored Door")
    newSelectedEntity = armoredDoor
    entityType = "Armored Door"
else:
    print("invalid Input")

selectedExplosive = input("Please select the the number that corresponds to the explosive you are trying to use: 1=Explosive Ammo, 2=C4, 3=Rockets ")
global newSelectedExplosive
global explosiveType
if selectedExplosive == "1":
    print("You selected: Explosive Ammo")
    newSelectedExplosive = Explo_Ammo_Damage
    explosiveType = "Explosive Ammo"
elif selectedExplosive == "2":
    print("You selected: C4")
    newSelectedExplosive = C4_Damage
    explosiveType = "C4"
elif selectedExplosive == "3":
    print("You selected: Rockets")
    newSelectedExplosive = Rocket_Damage
    explosiveType = "Rockets"
else:
    print("invalid Input")

def raidCostFunction(a, b):
    return(math.floor(a/b))

def intRaidCost (a, b):
    return(a/b)

def totalRaidCost (a, b):
    return(abs(a-b))

def multCost (a, b):
    return(a*b)

def megaCost(a, b, c,):
    return(c-(a*b))
initialRaidCost = raidCostFunction(newSelectedEntity, newSelectedExplosive)
actualRaidCost = intRaidCost(newSelectedEntity, newSelectedExplosive)
difRaidCost = totalRaidCost(initialRaidCost, actualRaidCost)

#print("initial", initialRaidCost)
#print(actualRaidCost)
#print(difRaidCost)
#print(initialRaidCost)
#print(newSelectedExplosive)
#print(newSelectedEntity)
#print(Explo_Ammo_Damage)

if difRaidCost != 0 and selectedExplosive != "1" and newSelectedExplosive < newSelectedEntity:
    difExploAmmo = megaCost(initialRaidCost, newSelectedExplosive, newSelectedEntity)
    exploOutput = multCost(difExploAmmo, Explo_Ammo_Damage)
    print("Your raid cost for a", entityType, "would be", initialRaidCost, explosiveType, "plus an additional", intRaidCost(difExploAmmo, 2), "explosive ammo" )
elif selectedExplosive == "1":
    print("Your raid cost for a", entityType, "would be", round(actualRaidCost), explosiveType)
elif selectedEntity == "1" and selectedExplosive == "1":
    print("Your raid cost for a", entityType, "would be 19", explosiveType)
elif selectedEntity == "1" and selectedExplosive == "3":
    print("Your raid cost for a", entityType, "would be 1", explosiveType)
elif selectedEntity == "1" and selectedExplosive == "2":
    print("Your raid cost for a", entityType, "would be 1", explosiveType)
else:
    print("Your raid cost for a", entityType, "would be", initialRaidCost, explosiveType)
>>>>>>> 053d2ca034de443d1b61e61bd848ad460b6fccff
