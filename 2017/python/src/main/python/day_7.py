import matplotlib.pyplot as plt
import networkx

with open('../resources/day7.input') as f:
    progs = {}
    has_parent = set()
    for line in f:
        line = line.strip().split()
        prog = (line[0], int(line[1][1:-1]))
        progs[prog] = []
        if '->' in line:
            idx = line.index('->')
            children = [c.strip(',') for c in line[idx + 1:]]
            progs[prog].extend(children)

    g = networkx.DiGraph()

    for program, children in progs.items():
        g.add_node(program[0], weight=program[1])
        for child in children:
            g.add_edge(program[0], child)

    sorted = list(networkx.topological_sort(g))

    plt.figure(1, figsize=(12, 12))

    # pos = networkx.spring_layout(g)

    networkx.draw_shell(g, with_labels=True, node_size=60, font_size=8)

    plt.show()


    # plt.savefig("image.png", bbox_inches='tight', dpi=150)

#     for node in reversed(ordered):
#     total = graph.nodes[node]['weight']
#
#     counts = collections.Counter(weights[child] for child in graph[node])
#     unbalanced = None
#
#     for child in graph[node]:
#         # If this child's weight is different than others, we've found it
#         if len(counts) > 1 and counts[weights[child]] == 1:
#             unbalanced = child
#             break
#
#         # Otherwise add to the total weight
#         val = weights[child]
#         total += weights[child]
#
#     if unbalanced:
#         # Find the weight adjustment and the new weight of this node
#         diff = weights[unbalanced] - val
#         print('PART 2:', graph.nodes[unbalanced]['weight'] - diff)
#         break
#
#     # Store the total weight of the node
# weights[node] = total
