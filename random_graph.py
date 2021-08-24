import networkx as nx
from matplotlib import pyplot as plt

gap = " , "


class RandomGraph():
    def __init__(self):
        self.g = nx.Graph()

    def read_graph(self):
        with open("attrs.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                tmp = line.strip().split(gap)
                self.g.add_node(tmp[0], type=tmp[1], gender=tmp[2],name=tmp[3], loc=tmp[4])
                self.g.add_node(tmp[-1])
                if not self.g.has_edge(tmp[0], tmp[-1]):
                    self.g.add_edge(tmp[0], tmp[-1], t_type=tmp[5], t_mode=tmp[6], t_channel=tmp[7], t_spending=tmp[8])
        self.g.remove_edges_from(nx.selfloop_edges(self.g))
        edge_labels = nx.get_edge_attributes(self.g, 't_type')
        node_labels = nx.get_node_attributes(self.g, 'type')

    def draw_graph(self):
        pos = nx.spring_layout(self.g)
        node_color = ['yellow' if self.g.nodes[v]["type"] == "商户" else 'red' for v in self.g]
        plt.figure(figsize=(20, 20))
        nx.draw_networkx(self.g, pos=pos, with_labels=False,
                         node_size=50, node_color=node_color)
        plt.axis('off')
        plt.show()
        # pos = nx.spring_layout(self.g)
        # nx.draw(self.g, pos)
        #node_labels = nx.get_node_attributes(self.g, 'type')
        #nx.draw_networkx_labels(self.g, pos, labels=node_labels)
        #edge_labels = nx.get_edge_attributes(self.g, 't_channel')
        #nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels)
        # plt.show()


if __name__ == '__main__':
    rg = RandomGraph()
    rg.read_graph()
    rg.draw_graph()
