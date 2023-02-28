# Caleb Verstraete
# 2/28/23
# CS325
import heapq

def main():
    G = [
 [0, 8, 5, 0, 0, 0, 0],
 [8, 0, 10, 2, 18, 0, 0],
 [5, 10, 0, 3, 0, 16, 0],
 [0, 2, 3, 0, 12, 30, 14],
 [0, 18, 0, 12, 0, 0, 4],
 [0, 0, 16, 30, 0, 0, 26],
 [0, 0, 0, 14, 4, 26, 0]
]

    print(Prims(G))


def Prims(G):
    mst = []
    pq = []
    visited_nodes = [0]

    # set up the priority queue with the nodes and edges connected to node 0
    for next_node in range(1, len(G[0])):
        if G[0][next_node]:
            heapq.heappush(pq, (G[0][next_node], next_node, 0))

    while len(visited_nodes) < len(G):
        smallest_edge, current_node, previous_node = heapq.heappop(pq)
        if current_node in visited_nodes and previous_node in visited_nodes:
            continue
        else:
            visited_nodes.append(current_node)
            mst.append((current_node, previous_node, smallest_edge))
        # check current nodes edges and add them to the pq
        for next_node in range(len(G[current_node])):
            if G[current_node][next_node] and next_node not in visited_nodes:
                heapq.heappush(pq, (G[current_node][next_node], next_node, current_node))

    return mst


if __name__ == '__main__':
    main()