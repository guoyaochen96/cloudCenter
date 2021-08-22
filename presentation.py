import networkx as nx
import matplotlib.pyplot as plt
from process_json import random_name


attributes = ["type", "gender", "name", "spending", "location"]
fb = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)


def generate_data():
    for v in fb:
        tmp = random_name()
        # print(tmp)
        with open("./attrs.txt", 'a', encoding="utf-8") as f:
            f.write(str(v) + ",")
            f.writelines(",".join(tmp))
            f.write("\n")
        for i in range(len(attributes)):
            fb.nodes[v][attributes[i]] = tmp[i]


with open("./attrs.txt", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        tmp = line.strip().split(",")
        for i in range(len(attributes)):
            fb.nodes[int(tmp[0])][attributes[i]] = tmp[i+1]


first_degree_connected_nodes = list(fb.neighbors(3437))
second_degree_connected_nodes = []
for x in first_degree_connected_nodes:
    second_degree_connected_nodes += list(fb.neighbors(x))
second_degree_connected_nodes.remove(3437)
second_degree_connected_nodes = list(set(second_degree_connected_nodes))
subgraph_3437 = nx.subgraph(fb,first_degree_connected_nodes+second_degree_connected_nodes)
betweennessCentrality = nx.betweenness_centrality(subgraph_3437, normalized=True, endpoints=True)
# node_size = [1000 if v == 3437 else 35 for v in subgraph_3437]


def draw_origin():
    pos = nx.spring_layout(subgraph_3437)
    node_color = ['yellow' if subgraph_3437.nodes[v]["type"] == "商户" else 'red' for v in subgraph_3437]
    plt.figure(figsize=(20,20))
    nx.draw_networkx(subgraph_3437, pos=pos, with_labels=False,
                     node_size=50, node_color=node_color)
    plt.axis('off')
    plt.show()


def draw_influence():
    pos = nx.spring_layout(subgraph_3437)
    top_center = sorted([v for v in betweennessCentrality], key=lambda x: betweennessCentrality[x], reverse=True)
    node_color = ['yellow' if subgraph_3437.nodes[v]["type"] == "商户" else 'red' for v in subgraph_3437]
    # node_color = ['yellow' if v in top_center[:4] else 'red' for v in subgraph_3437]
    node_size = [v * 3000 for v in betweennessCentrality.values()]
    plt.figure(figsize=(20,20))
    nx.draw_networkx(subgraph_3437, pos=pos, with_labels=False,
                     node_size=node_size, node_color=node_color)
    plt.axis('off')
    plt.show()


def candidate_list(query):
    candidates = [v for v in subgraph_3437 if query in subgraph_3437.nodes[v]["location"]]
    if len(candidates) == 0:
        return []
    ans = sorted(candidates, key= lambda x: betweennessCentrality[x], reverse=True)[0]
    res = []
    for attr in attributes:
        res.append(subgraph_3437.nodes[ans][attr])
    return res


if __name__ == '__main__':
    candidate_list("浦东新区")