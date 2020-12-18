from enum import Enum


class NodeType(Enum):
    sensor = 0
    hidden = 1
    output = 2


class Node:
    def __init__(self, index: int, node_type: NodeType, bias: float):
        self.index = index
        self.type = node_type
        self.bias = bias
