from neevo.Node import Node, NodeType


class Network:
    # nodes = {}

    def __init__(self, *args: int):
        """
        initializes layered base network
        :param args: numbers of nodes for every layer
        """
        self.nodes = dict()
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

                # organize nodes into layers
                layers[index].append(global_index)

                global_index += 1

    def add_node(self, node):
        if isinstance(node, Node) and node.index not in self.nodes:
            self.nodes[node.index] = node