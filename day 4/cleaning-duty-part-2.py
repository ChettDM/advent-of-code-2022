import os

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()

total = 0
for assignments in lines:
    assignments = assignments.strip()

    splitAssignments = assignments.split(",")
    firstElfsAssignment = splitAssignments[0].split("-")
    secondElfsAssignment = splitAssignments[1].split("-")

    if int(secondElfsAssignment[0]) <= int(firstElfsAssignment[0]) <= int(secondElfsAssignment[1]):
        total += 1
        continue

    if int(firstElfsAssignment[0]) <= int(secondElfsAssignment[0]) <= int(firstElfsAssignment[1]):
        total += 1
        continue

print(total)
