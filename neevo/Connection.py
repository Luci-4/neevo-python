from neevo.Node import Node


class Connection:
    def __init__(self, index: tuple, start_node: Node, end_node: Node, weight: float):
        self.index = index
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
