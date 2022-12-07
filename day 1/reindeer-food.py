import os

data = open(os.path.join(os.path.dirname(__file__),'data.txt'),'r')
lines = data.readlines()
calorieTotals = [0]
calorieCountIndex = 0

for line in lines:
    try:
        item = int(line.strip())
        calorieTotals[calorieCountIndex] += item
    except:
        calorieTotals.append(0)
        calorieCountIndex += 1

calorieTotals.pop()

calorieTotals.sort(reverse=True)

print("total")
print(calorieCountIndex)

print("all toals")
print(calorieTotals)

print("largest total")
print(calorieTotals[0] + calorieTotals[1] + calorieTotals[2])
