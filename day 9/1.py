import os
from Knot import Knot
from Node import Node

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()




def print_map(start, head=None, tail=None):
    should_print = True

    os.system('clear')
    row = start
    while row.Up is not None:
        row = row.Up

    while row is not None:
        column = row
        output = ""

        while column is not None:
            word = " . "

            if head is not None and tail is not None:
                if start.Id == column.Id:
                    word = " S "

                if tail.CurrentPosition.Id == column.Id:
                    word = " T "

                if head.CurrentPosition.Id == column.Id:
                    word = " H "

            output += word
            column = column.Right

        if should_print:
            print(output)
        row = row.Down


nodes = []
grid_size = 50

for column in range(grid_size):
    rows = []
    for row in range(grid_size):
        rows.append(Node())
    nodes.append(rows)

for columns in range(grid_size):
    for rows in range(grid_size):
        if columns-1 >= 0:
            nodes[columns][rows].Left = nodes[columns-1][rows]

        if rows-1 >= 0:
            nodes[columns][rows].Up = nodes[columns][rows-1]

        if columns+1 < grid_size:
            nodes[columns][rows].Right = nodes[columns+1][rows]

        if rows+1 < grid_size:
            nodes[columns][rows].Down = nodes[columns][rows+1]

print_map(nodes[0][0])
print()

# setup
# grid_size = 50
# grid = start = Node()
# for _ in range(grid_size):
#     grid.Right = Node()
#     grid.Right.Left = grid
#     grid = grid.Right
#
#
#
#
#
# current_row = grid = start
# for _ in range(grid_size):
#     current_row = grid
#     current_row.Down = Node()
#     current_row.Down.Up = current_row
#     current_row = current_row.Down
#     grid = current_row
#
#     for _ in range(grid_size - 1):
#         current_row
#
#     # creaating them down
#     one.Down = Node()
#     one.Down.Up = one
#     one = one.Down
#
#     two.Down = Node()
#     two.Down.Up = two
#     two = two.Down
#
#     three.Down = Node()
#     three.Down.Up = three
#     three = three.Down
#
#     four.Down = Node()
#     four.Down.Up = four
#     four = four.Down
#
#     five.Down = Node()
#     five.Down.Up = five
#     five = five.Down
#
#     six.Down = Node()
#     six.Down.Up = six
#     six = six.Down
#
#     # connecting them accross
#     one.Right = two
#     two.Left = one
#     two.Right = three
#     three.Left = two
#     three.Right = four
#     four.Left = three
#     four.Right = five
#     five.Left = four
#     five.Right = six
#     six.Left = five
#
# start = grid.Down.Down.Down.Down

start = grid = nodes[grid_size-1][0]

head_knot = Knot()
tail_knot = Knot()

head_knot.CurrentPosition = start
tail_knot.CurrentPosition = start
tail_knot.CurrentPosition.Visited = True

print_map(grid, head_knot, tail_knot)

# end of setup

def tail_is_next_to_head(head, tail):
    if head.Id == tail.Id:
        return True

    if head.Left is not None:
        if head.Left.Id == tail.Id:
            return True
        if head.Left.Up is not None and head.Left.Up.Id == tail.Id:
            return True
        if head.Left.Down is not None and head.Left.Down.Id == tail.Id:
            return True

    if head.Up is not None:
        if head.Up.Id == tail.Id:
            return True
        if head.Up.Left is not None and head.Up.Left.Id == tail.Id:
            return True
        if head.Up.Right is not None and head.Up.Right.Id == tail.Id:
            return True

    if head.Right is not None:
        if head.Right.Id == tail.Id:
            return True
        if head.Right.Up is not None and head.Right.Up.Id == tail.Id:
            return True
        if head.Right.Down is not None and head.Right.Down.Id == tail.Id:
            return True

    if head.Down is not None:
        if head.Down.Id == tail.Id:
            return True
        if head.Down.Left is not None and head.Down.Left.Id == tail.Id:
            return True
        if head.Down.Right is not None and head.Down.Right.Id == tail.Id:
            return True





def count_visits(start):
    total = 0
    row = start
    while row.Up is not None:
        row = row.Up

    while row is not None:
        column = row

        while column is not None:
            if column.Visited:
                total += 1
            column = column.Right

        row = row.Down

    return total


print_map(start, head_knot, tail_knot)

for line in lines:
    line = line.strip()
    command = line.split(" ")
    direction = command[0]
    moves = int(command[1])

    match direction:
        case "R":
            for _ in range(moves):
                head_knot.CurrentPosition = head_knot.CurrentPosition.Right
                if not tail_is_next_to_head(head_knot.CurrentPosition, tail_knot.CurrentPosition):
                    tail_knot.CurrentPosition = head_knot.CurrentPosition.Left
                    tail_knot.CurrentPosition.Visited = True
                # print_map(start, head_knot, tail_knot)
        case "L":
            for _ in range(moves):
                head_knot.CurrentPosition = head_knot.CurrentPosition.Left
                if not tail_is_next_to_head(head_knot.CurrentPosition, tail_knot.CurrentPosition):
                    tail_knot.CurrentPosition = head_knot.CurrentPosition.Right
                    tail_knot.CurrentPosition.Visited = True
                # print_map(start, head_knot, tail_knot)
        case "U":
            for _ in range(moves):
                head_knot.CurrentPosition = head_knot.CurrentPosition.Up
                if not tail_is_next_to_head(head_knot.CurrentPosition, tail_knot.CurrentPosition):
                    tail_knot.CurrentPosition = head_knot.CurrentPosition.Down
                    tail_knot.CurrentPosition.Visited = True
                # print_map(start, head_knot, tail_knot)
        case "D":
            for _ in range(moves):
                head_knot.CurrentPosition = head_knot.CurrentPosition.Down
                if not tail_is_next_to_head(head_knot.CurrentPosition, tail_knot.CurrentPosition):
                    tail_knot.CurrentPosition = head_knot.CurrentPosition.Up
                    tail_knot.CurrentPosition.Visited = True
                # print_map(start, head_knot, tail_knot)

    # print_map(start, head_knot, tail_knot)

print(count_visits(start))
