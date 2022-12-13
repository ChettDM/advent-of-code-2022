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


def calculate_tree_view(row_index, column_index):
    right = forest[row_index][column_index+1:]
    left = forest[row_index][:column_index]
    top = [item[column_index] for item in forest[:row_index]]
    bottom = [item[column_index] for item in forest[row_index+1:]]

    # print(right)
    # print(left)
    # print(top)
    # print(bottom)

    right_count = 0
    for tree in right:
        right_count += 1
        if tree >= forest[row_index][column_index]:
            break

    left_count = 0
    for tree in list(reversed(left)):
        left_count += 1
        if tree >= forest[row_index][column_index]:
            break

    bottom_count = 0
    for tree in bottom:
        bottom_count += 1
        if tree >= forest[row_index][column_index]:
            break

    top_count = 0
    for tree in list(reversed(top)):
        top_count += 1
        if tree >= forest[row_index][column_index]:
            break

    # print(right_count)
    # print(left_count)
    # print(bottom_count)
    # print(top_count)

    return right_count * left_count * bottom_count * top_count


best = 0
for i in range(1, len(forest) -1):
    for j in range(1, len(forest[0]) - 1):
        coverage = calculate_tree_view(i, j)
        if coverage > best:
            best = coverage
        # if not is_not_visible(i, j):
        #     total += 1

print(best)