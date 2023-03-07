# Caleb Verstraete
# 3/7/23
# CS325
# Use nearest neighbor heuristic to solve the Traveling sales person (TSP) problem. Given a graph and starting at
# position 0 travel to the closest neighbor. You can only visit a position once except the starting point.


def main():
    G = [
        [0, 2, 3, 20, 1],
        [2, 0, 15, 2, 20],
        [3, 15, 0, 20, 13],
        [20, 2, 20, 0, 9],
        [1, 20, 13, 9, 0],
    ]

    print(solve_tsp(G))


def solve_tsp(G):
    # result with starting point
    result = [0]
    current_neighbor = 0

    visited = []
    # while loop to travel to each node
    while len(visited) < len(G) - 1:
        nearest_neighbor = 0
        smallest_edge = float('inf')
        visited.append(current_neighbor)
        # for loop over edges to find smallest non-visited neighbor
        for edge in range(len(G[current_neighbor])):
            if 0 < G[current_neighbor][edge] < smallest_edge and edge not in visited:
                smallest_edge = G[current_neighbor][edge]
                nearest_neighbor = edge
        result.append(nearest_neighbor)
        current_neighbor = nearest_neighbor
    # Add start node to result path and return result
    result.append(0)
    return result


if __name__ == '__main__':
    main()