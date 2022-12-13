import os

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()

forest = []

for line in lines:
    line = line.strip()
    row = []

    for number in line:
        row.append(int(number))

    forest.append(row)


def is_not_visible(row_index, column_index):
    # doesn't work because it's a 3d array
    right = [item for item in forest[row_index][column_index+1:] if item >= forest[row_index][column_index]]
    left = [item for item in forest[row_index][:column_index] if item >= forest[row_index][column_index]]
    top = [item for item in forest[:row_index] if item[column_index] >= forest[row_index][column_index]]
    bottom = [item for item in forest[row_index+1:] if item[column_index] >= forest[row_index][column_index]]

    # print(right)
    # print(left)
    # print(top)
    # print(bottom)

    return len(right) > 0 and len(left) > 0 and len(top) > 0 and len(bottom) > 0


total = (len(forest) * 2) + (len(forest[0]) * 2) - 4
# print(total)
for i in range(1, len(forest) -1):
    for j in range(1, len(forest[0]) - 1):
        if not is_not_visible(i, j):
            total += 1

print(total)