import os

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()

startingCrateConfiguration = lines[0:8]
crateMovements = lines[10:]


def add_non_blank_value_to_array(array: [], item: str):
    item = item.strip()
    if len(item):
        array.append(item)


def convert_crate_configuration_to_model(crate_configuration: []) -> [[]]:
    crate_model = []

    for i in range(9):
        crate_model.append([])

    for i in range(len(crate_configuration) - 1, -1, -1):
        add_non_blank_value_to_array(crate_model[0], crate_configuration[i][0:3])
        add_non_blank_value_to_array(crate_model[1], crate_configuration[i][4:7])
        add_non_blank_value_to_array(crate_model[2], crate_configuration[i][8:11])
        add_non_blank_value_to_array(crate_model[3], crate_configuration[i][12:15])
        add_non_blank_value_to_array(crate_model[4], crate_configuration[i][16:19])
        add_non_blank_value_to_array(crate_model[5], crate_configuration[i][20:23])
        add_non_blank_value_to_array(crate_model[6], crate_configuration[i][24:27])
        add_non_blank_value_to_array(crate_model[7], crate_configuration[i][28:31])
        add_non_blank_value_to_array(crate_model[8], crate_configuration[i][32:35])

    return crate_model


def print_crate_model(crate_model: [[]]):
    for slot in crate_model:
        row = ""

        for crates in slot:
            row += crates

        print("|" + row)


def break_movement_procedure_down(instruction: str) -> any:
    instruction_set = instruction.strip().split(" ")
    # print(instruction_set)
    return int(instruction_set[1]), int(instruction_set[3]) - 1, int(instruction_set[5]) - 1


def simulate_movements(crate_movements: [], crate_model: [[]]):
    # print_crate_model(crate_model)
    # print()
    for instruction in crate_movements:
        number_to_move, from_index, to_index = break_movement_procedure_down(instruction)

        temp_list = []
        for _ in range(number_to_move):
            temp_list.append(crate_model[from_index].pop())

        for _ in range(number_to_move):
            crate_model[to_index].append(temp_list.pop())

        # print_crate_model(crate_model)
        # print()


def print_top_crates(model: [[]]):
    top_crate_list = ""
    for column in model:
        if len(column) <= 0:
            top_crate_list += "   "
            continue

        top_crate_list += column[len(column) - 1]

    print(top_crate_list.replace("[", "").replace("]", ""))


model = convert_crate_configuration_to_model(startingCrateConfiguration)

print_top_crates(model)
# print_crate_model(model)
print()

simulate_movements(crateMovements, model)
# print()

# print_crate_model(model)
# print()

print_top_crates(model)