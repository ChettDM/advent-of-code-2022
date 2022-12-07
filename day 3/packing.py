import os

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()


def itemIsInCompartment(compartment, item):
    try:
        compartment.index(item)
        return True
    except:
        return False


def findItem(backpack1, backpack2, backpack3):
    for item in backpack1:
        if itemIsInCompartment(backpack2, item) and itemIsInCompartment(backpack3, item):
            return item


def getPriority(character):
    characterValue = ord(character)

    if characterValue >= 65 and characterValue <= 90:  # Uppercase
        return characterValue - 38
    if characterValue >= 97 and characterValue <= 122:  # lowercase
        return characterValue - 96


total = 0
for i in range(0, len(lines), 3):
    backpack1 = lines[i].strip()
    backpack2 = lines[i + 1].strip()
    backpack3 = lines[i + 2].strip()

    foundItem = findItem(backpack1, backpack2, backpack3)

    total += getPriority(foundItem)

print(total)

# def findMisplacedItemsIndex(compartmentA, compartmentB):
#     for item in compartmentA:
#         try:
#             return compartmentB.index(item)
#         except:
#             pass
#     return -1


# def getScore(character):
#     characterValue = ord(character)

#     if characterValue >= 65 and characterValue <= 90:  # Uppercase
#         return characterValue - 38
#     if characterValue >= 97 and characterValue <= 122:  # lowercase
#         return characterValue - 96


# total = 0
# for items in lines:
#     items = items.strip()
#     numberOfItems = len(items)
#     compartment1 = items[0:numberOfItems//2]
#     compartment2 = items[numberOfItems//2:]

#     index = findMisplacedItemsIndex(compartment1, compartment2)
#     if index > 0:
#         value = getScore(compartment2[index])
#         total += value
#         continue

#     index = findMisplacedItemsIndex(compartment2, compartment1)
#     if index > 0:
#         value = getScore(compartment1[index])
#         total += value
#         continue

# print(total)
