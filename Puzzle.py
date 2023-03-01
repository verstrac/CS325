# Caleb Verstraete
# 3/1/23
# CS325
import heapq


def main():
    board = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]
    source = (0, 0)
    destination = (4, 4)
    print(solve_board(board, source, destination))


def calc_destination_to_distance(destination, new_node):
    row_distance = abs(new_node[0] - destination[0])
    col_distance = abs(new_node[1] - destination[1])
    return row_distance + col_distance


def check_down(current_pos, pq, board, visited_nodes, destination, path):
    possible_path = path.copy()
    down_pos_row = current_pos[0] + 1
    down_pos_col = current_pos[1]
    if down_pos_row < len(board) and (down_pos_row, down_pos_col) not in visited_nodes:
        if board[down_pos_row][down_pos_col] != '#':
            distance_to_destination = calc_destination_to_distance(destination, (down_pos_row, down_pos_col))
            possible_path.append((down_pos_row, down_pos_col))
            heapq.heappush(pq, (distance_to_destination, (down_pos_row, down_pos_col), 'U', possible_path))


def check_up(current_pos, pq, board, visited_nodes, destination, path):
    possible_path = path.copy()
    up_pos_row = current_pos[0] - 1
    up_pos_col = current_pos[1]
    if up_pos_row >= 0 and (up_pos_row, up_pos_col) not in visited_nodes:
        if board[up_pos_row][up_pos_col] != '#':
            distance_to_destination = calc_destination_to_distance(destination, (up_pos_row, up_pos_col))
            possible_path.append((up_pos_row, up_pos_col))
            heapq.heappush(pq, (distance_to_destination, (up_pos_row, up_pos_col), 'D', possible_path))


def check_left(current_pos, pq, board, visited_nodes, destination, path):
    possible_path = path.copy()
    left_pos_row = current_pos[0]
    left_pos_col = current_pos[1] - 1
    if left_pos_col >= 0 and (left_pos_row, left_pos_col) not in visited_nodes:
        if board[left_pos_row][left_pos_col] != '#':
            distance_to_destination = calc_destination_to_distance(destination, (left_pos_row, left_pos_col))
            possible_path.append((left_pos_row, left_pos_col))
            heapq.heappush(pq, (distance_to_destination, (left_pos_row, left_pos_col), 'R', possible_path))


def check_right(current_pos, pq, board, visited_nodes, destination, path):
    possible_path = path.copy()
    right_pos_row = current_pos[0]
    right_pos_col = current_pos[1] + 1
    if right_pos_col < len(board[0]) and (right_pos_row, right_pos_col) not in visited_nodes:
        if board[right_pos_row][right_pos_col] != '#':
            distance_to_destination = calc_destination_to_distance(destination, (right_pos_row, right_pos_col))
            possible_path.append((right_pos_row, right_pos_col))
            heapq.heappush(pq, (distance_to_destination, (right_pos_row, right_pos_col), 'L', possible_path))


def solve_board(board, source, destination):
    pq = [(0, source, None, [source])]
    visited_nodes = []

    while len(pq) > 0:
        # Pop off the position that gets us closer to the destination
        distance_to_destination, current_node, previous_node, cur_path = heapq.heappop(pq)
        # if node has already been visited no need to check around it again
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
        else:
            continue
        # check if target is reached
        if current_node == destination:
            return cur_path
        # check neighbors except edge where we came from
        if previous_node != 'D':
            check_down(current_node, pq, board, visited_nodes, destination, cur_path)
        if previous_node != 'R':
            check_right(current_node, pq, board, visited_nodes, destination, cur_path)
        if previous_node != 'U':
            check_up(current_node, pq, board, visited_nodes, destination, cur_path)
        if previous_node != 'L':
            check_left(current_node, pq, board, visited_nodes, destination, cur_path)


if __name__ == '__main__':
    main()