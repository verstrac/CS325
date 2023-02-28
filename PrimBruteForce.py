'''
Implement a function prims(G)

Example:
G = [[0, 9, 75, 0, 0],
         [9, 0, 95, 19, 42],
         [75, 95, 0, 51, 66],
         [0, 19, 51, 0, 31],
         [0, 42, 66, 31, 0]]

prims(G)

would print

Edge : Weight
0-1:9
1-3:19
3-4:31
3-2:51
'''


def main():
    print(prim_brute_force([[0, 9, 75, 0, 0],
                      [9, 0, 95, 19, 42],
                      [75, 95, 0, 51, 66],
                      [0, 19, 51, 0, 31],
                      [0, 42, 66, 31, 0]]))


def prim_brute_force(graph):
    shortest_paths = {}
    for vertex in range(len(graph) - 1):
        shortest_path = float('inf')
        second_vertex = None
        for connected_vertex in range(vertex + 1, len(graph[vertex])):
            if 0 < graph[vertex][connected_vertex] < shortest_path:
                shortest_path = graph[vertex][connected_vertex]
                second_vertex = connected_vertex
        shortest_paths[(vertex, second_vertex)] = shortest_path
    return shortest_paths


if __name__ == '__main__':
    main()