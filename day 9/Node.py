import uuid


class Node:
    def __init__(self):
        self.Up = None
        self.Down = None
        self.Right = None
        self.Left = None
        self.Visited = False
        self.Id = uuid.uuid4()
