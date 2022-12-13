import os
from Directory import Directory
from File import File

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()


current_directory = root_directory = Directory("/", None)

for line in lines[1:]:
    line = line.strip()
    # print(line)
    command = line.split(" ")

    match command[0]:
        case "$": # commandss
            if command[1] == "cd":
                if command[2] == "..":
                    current_directory = current_directory.Parent
                else:
                    for child in current_directory.Children:
                        if child.Name == command[2] and isinstance(child, Directory):
                            current_directory = child
                            break
        case "dir": # directories
            current_directory.add_directory(command[1])
        case _: # files
            current_directory.add_file(command[1], command[0])


def print_file_tree(node, spacer=""):
    if isinstance(node, Directory):
        print(spacer + " -D " + node.Name)

        for c in node.Children:
            print_file_tree(c, spacer + " ")

    elif isinstance(node, File):
        print(spacer + " -F " + node.Name + " | " + str(node.Size))


class Calculate:
    total = 0

    def __init__(self):
        pass

    def print_total(self):
        print(self.total)

    def calculate_folder_sizes(self, node):
        if isinstance(node, File):
            # print("file-" + str(node.Size))
            return node.Size

        elif isinstance(node, Directory):
            directory_total = 0
            # print("~~" + node.Name + "~~")

            for c in node.Children:
                file_size = self.calculate_folder_sizes(c)
                # print(c.Name + " - " + str(file_size))
                directory_total += file_size

            # print("~~" + node.Name + "~~")
            # print()
            if directory_total < 100000:
                self.total += directory_total

            return directory_total





calculate = Calculate()
calculate.calculate_folder_sizes(root_directory)
calculate.print_total()
# print_file_tree(root_directory)