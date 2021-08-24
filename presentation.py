import random

import networkx as nx
import matplotlib.pyplot as plt
from process_json import random_name, random_transaction


class readData:
    def __init__(self):
        self.attributes = ["user_type", "gender", "name", "location", "transaction_type", "transaction_mode",
                           "Transaction channel", "spending"]
        self.fb = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)
        self.subgraph_3437 = nx.Graph()

    def generate_data(self):
        vertexs = list(self.fb.nodes)
        gap , col = " , ", " | "
            # print(tmp)
        with open("./attrs.txt", 'a', encoding="utf-8") as f:
            f.writelines("编号" + col + "类型" + col + "性别" + col + "姓名" + col + "位置" + col + "交易类型" + col + "交易方式" + col + "交易渠道" + col + "编号" + "\n")
            for v in self.fb:
                tmp1 = random_name()
                for i in range(random.randint(1, 10)):
                    tmp2 = random_transaction(tmp1[0])
                    f.write(str(v) + gap)
                    f.writelines(gap.join(tmp1) + gap + gap.join(tmp2))
                    cnnt = str(random.choice(vertexs))
                    if tmp1[0] == "商户":
                        cnnt = str(v)

                    f.write(gap + cnnt)
                    f.write("\n")
                    if tmp1[0] == "商户":
                        break

    def read_graph(self):
        with open("./attrs.txt", 'r', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                tmp = line.strip().split(",")
                for i in range(len(self.attributes)):
                    self.fb.nodes[int(tmp[0])][self.attributes[i]] = tmp[i + 1]

        first_degree_connected_nodes = list(self.fb.neighbors(3437))
        second_degree_connected_nodes = []
        for x in first_degree_connected_nodes:
            second_degree_connected_nodes += list(self.fb.neighbors(x))
        second_degree_connected_nodes.remove(3437)
        second_degree_connected_nodes = list(set(second_degree_connected_nodes))
        self.subgraph_3437 = nx.subgraph(self.fb, first_degree_connected_nodes + second_degree_connected_nodes)

    # node_size = [1000 if v == 3437 else 35 for v in subgraph_3437]

    def draw_origin(self):
        pos = nx.spring_layout(self.subgraph_3437)
        node_color = ['yellow' if self.subgraph_3437.nodes[v]["type"] == "商户" else 'red' for v in self.subgraph_3437]
        plt.figure(figsize=(20, 20))
        nx.draw_networkx(self.subgraph_3437, pos=pos, with_labels=False,
                         node_size=50, node_color=node_color)
        plt.axis('off')
        plt.show()

    def draw_influence(self):
        pos = nx.spring_layout(self.subgraph_3437)
        betweennessCentrality = nx.betweenness_centrality(self.subgraph_3437, normalized=True, endpoints=True)
        top_center = sorted([v for v in betweennessCentrality], key=lambda x: betweennessCentrality[x], reverse=True)
        node_color = ['yellow' if self.subgraph_3437.nodes[v]["type"] == "商户" else 'red' for v in self.subgraph_3437]
        # node_color = ['yellow' if v in top_center[:4] else 'red' for v in subgraph_3437]
        node_size = [v * 3000 for v in betweennessCentrality.values()]
        plt.figure(figsize=(20, 20))
        nx.draw_networkx(self.subgraph_3437, pos=pos, with_labels=False,
                         node_size=node_size, node_color=node_color)
        plt.axis('off')
        plt.show()

    def candidate_list(self, query):
        betweennessCentrality = nx.betweenness_centrality(self.subgraph_3437, normalized=True, endpoints=True)
        candidates = [v for v in self.subgraph_3437 if query in self.subgraph_3437.nodes[v]["location"]]
        if len(candidates) == 0:
            return []
        ans = sorted(candidates, key=lambda x: betweennessCentrality[x], reverse=True)[0]
        res = []
        for attr in self.attributes:
            res.append(self.subgraph_3437.nodes[ans][attr])
        return res


if __name__ == '__main__':
    tmp = readData()
    tmp.generate_data()
