import os
from Directory import Directory
from File import File

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()


class Calculate:
    def __init__(self):
        self.total = 0

        self.total_file_system_size = self.current_freespace = 70000000
        self.needed_free_space = 30000000
        self.deletion_candidates = []
        self.current_directory = self.root_directory = Directory("/", None)

        for line in lines[1:]:
            line = line.strip()
            command = line.split(" ")

            match command[0]:
                case "$": # commandss
                    if command[1] == "cd":
                        if command[2] == "..":
                            self.current_directory = self.current_directory.Parent
                        else:
                            for child in self.current_directory.Children:
                                if child.Name == command[2] and isinstance(child, Directory):
                                    self.current_directory = child
                                    break
                case "dir": # directories
                    self.current_directory.add_directory(command[1])
                case _: # files
                    self.current_freespace -= int(command[0])
                    self.current_directory.add_file(command[1], command[0])

    @staticmethod
    def print_file_tree(node, spacer=""):
        if isinstance(node, Directory):
            print(spacer + " -D " + node.Name)

            for c in node.Children:
                Calculate.print_file_tree(c, spacer + " ")

        elif isinstance(node, File):
            print(spacer + " -F " + node.Name + " | " + str(node.Size))

    def print_total(self):
        print(self.total)

    def calculate_folder_sizes(self, node):
        if isinstance(node, File):
            return node.Size

        elif isinstance(node, Directory):
            directory_total = 0

            for c in node.Children:
                file_size = self.calculate_folder_sizes(c)
                directory_total += file_size

            if directory_total + calculate.current_freespace - calculate.needed_free_space > 0:
                self.deletion_candidates.append(directory_total)

            if directory_total < 100000:
                self.total += directory_total

            return directory_total

    def find_folder_for_size(self, node):
        if isinstance(node, File):
            return node.Size

        elif isinstance(node, Directory):
            directory_total = 0

            for c in node.Children:
                file_size = self.calculate_folder_sizes(c)
                directory_total += file_size

            if directory_total < 100000:
                self.total += directory_total

            return directory_total


calculate = Calculate()
Calculate.print_file_tree(calculate.root_directory)

print()

print(calculate.current_freespace)
print(calculate.current_freespace - calculate.needed_free_space)

print()

calculate.calculate_folder_sizes(calculate.root_directory)

smallest_size = calculate.total_file_system_size
for item in calculate.deletion_candidates:
    if int(item) < smallest_size:
        smallest_size = int(item)

print(smallest_size)
# calculate.calculate_folder_sizes(root_directory)
# calculate.print_total()
# print_file_tree(root_directory)

24933642