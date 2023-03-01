# Caleb Verstraete
# 3/1/23
# CS325
# Code adapted from MinPuzzle.py, Date: 2/23/23
# Author Caleb Verstraete


import heapq


def main():
    board = [
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '-', '-'],
        ['#', '-', '#', '-', '-'],
        ['#', '-', '-', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]
    source = (0, 0)
    destination = (4, 0)
    print(solve_puzzle(board, source, destination))


def check_down(current_pos, pq, board, visited_nodes, destination, path, str_path):
    possible_path = path.copy()
    possible_str_path = str_path
    down_pos_row = current_pos[0] + 1
    down_pos_col = current_pos[1]
    if down_pos_row < len(board) and (down_pos_row, down_pos_col) not in visited_nodes:
        if board[down_pos_row][down_pos_col] != '#':
            possible_path.append((down_pos_row, down_pos_col))
            possible_str_path += 'D'
            heapq.heappush(pq, (len(possible_path), (down_pos_row, down_pos_col), 'U', possible_path, possible_str_path))


def check_up(current_pos, pq, board, visited_nodes, destination, path, str_path):
    possible_path = path.copy()
    possible_str_path = str_path
    up_pos_row = current_pos[0] - 1
    up_pos_col = current_pos[1]
    if up_pos_row >= 0 and (up_pos_row, up_pos_col) not in visited_nodes:
        if board[up_pos_row][up_pos_col] != '#':
            possible_path.append((up_pos_row, up_pos_col))
            possible_str_path += 'U'
            heapq.heappush(pq, (len(possible_path), (up_pos_row, up_pos_col), 'D', possible_path, possible_str_path))


def check_left(current_pos, pq, board, visited_nodes, destination, path, str_path):
    possible_path = path.copy()
    possible_str_path = str_path
    left_pos_row = current_pos[0]
    left_pos_col = current_pos[1] - 1
    if left_pos_col >= 0 and (left_pos_row, left_pos_col) not in visited_nodes:
        if board[left_pos_row][left_pos_col] != '#':
            possible_path.append((left_pos_row, left_pos_col))
            possible_str_path += 'L'
            heapq.heappush(pq, (len(possible_path), (left_pos_row, left_pos_col), 'R', possible_path, possible_str_path))


def check_right(current_pos, pq, board, visited_nodes, destination, path, str_path):
    possible_path = path.copy()
    possible_str_path = str_path
    right_pos_row = current_pos[0]
    right_pos_col = current_pos[1] + 1
    if right_pos_col < len(board[0]) and (right_pos_row, right_pos_col) not in visited_nodes:
        if board[right_pos_row][right_pos_col] != '#':
            possible_path.append((right_pos_row, right_pos_col))
            possible_str_path += 'R'
            heapq.heappush(pq, (len(possible_path), (right_pos_row, right_pos_col), 'L', possible_path, possible_str_path))


def solve_puzzle(board, source, destination):
    pq = [(0, source, None, [source], '')]
    visited_nodes = []
    node_dict = {source: [source]}

    while len(pq) > 0:
        # Pop off the position that gets us closer to the destination
        distance_to_destination, current_node, previous_node, cur_path, str_path = heapq.heappop(pq)
        # if node has already been visited no need to check around it again
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
        else:
            continue
        # check if target is reached
        if current_node == destination:
            return cur_path, str_path
        # check neighbors except edge where we came from
        if previous_node != 'D':
            check_down(current_node, pq, board, visited_nodes, destination, cur_path, str_path)
        if previous_node != 'R':
            check_right(current_node, pq, board, visited_nodes, destination, cur_path, str_path)
        if previous_node != 'U':
            check_up(current_node, pq, board, visited_nodes, destination, cur_path, str_path)
        if previous_node != 'L':
            check_left(current_node, pq, board, visited_nodes, destination, cur_path, str_path)


if __name__ == '__main__':
    main()