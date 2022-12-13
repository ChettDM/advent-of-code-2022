from Node import Node


class File(Node):
    def __init__(self, name, parent_directory, size):
        super().__init__(name=name, parent_node=parent_directory)

        self.Size = size
