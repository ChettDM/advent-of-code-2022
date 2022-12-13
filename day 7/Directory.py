from Node import Node
from File import File


class Directory(Node):
    def __init__(self, name, parent_directory):
        super().__init__(name=name, parent_node=parent_directory)
        self.Children = []

    def add_file(self, name, size):
        self.Children.append(File(name, self, int(size)))

    def add_directory(self, name):
        self.Children.append(Directory(name, self))