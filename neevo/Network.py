import numpy as np
from neevo.Node import Node, NodeType
from neevo.Connection import Connection


class Network:

    def __init__(self, *args: int):
        """
        initializes layered base network
        :param args: numbers of nodes for every layer
        """
        self.nodes = dict()
        self.nodes_indices = list()
        self.connections = dict()
        global_index = 0

        layers = [list() for _ in args]

        # for every layer
        for index, n_nodes in enumerate(args):
            if index == 0:
                node_type = NodeType(0)

            elif index == len(args) - 1:
                node_type = NodeType(2)

            else:
                node_type = NodeType(1)

            # create nodes
            for n_node in range(args[index]):
                node = Node(global_index, node_type, 0)
                self.add_node(node)

                # organize nodes' indexes into layers
                layers[index].append(global_index)

                global_index += 1

        # create connections
        for layer_index in range(1, len(layers)):
            for node1_index in layers[layer_index - 1]:
                for node2_index in layers[layer_index]:

                    # get Node instances
                    node1 = self.nodes[node1_index]
                    node2 = self.nodes[node2_index]

                    weight = np.random.randn()

                    connection = Connection((node1_index, node2_index), node1, node2, weight)
                    self.add_connection(connection)

    def add_node(self, node):
        if isinstance(node, Node) and node.index not in self.nodes:
            self.nodes[node.index] = node

    def add_connection(self, connection: Connection):
        if isinstance(connection, Connection):
            self.connections[connection.index] = connection
