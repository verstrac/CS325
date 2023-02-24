# Caleb Verstraete
# 2/23/23
# CS325
# Code adapted from OSU Canvas module 47.3 CS325 Dijkstra's algorithm calculate distance
# 02/23/2023
# https://canvas.oregonstate.edu/courses/1901711/pages/exploration-7-dot-3-dijkstras-algorithm?module_item_id=22792907
import heapq


def main():
    print(minEffort([[1, 1, 5],
                     [1, 1, 9],
                     [4, 4, 5]]))


def checkDown(current_pos, pq, puzzle, visited_nodes):
    down_pos_row = current_pos[0] + 1
    down_pos_col = current_pos[1]
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if down_pos_row < len(puzzle) and (down_pos_row, down_pos_col) not in visited_nodes:
        down_pos_height = puzzle[down_pos_row][down_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - down_pos_height), (down_pos_row, down_pos_col), 'UP'))


def checkUp(current_pos, pq, puzzle, visited_nodes):
    up_pos_row = current_pos[0] - 1
    up_pos_col = current_pos[1]
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if up_pos_row >= 0 and (up_pos_row, up_pos_col) not in visited_nodes:
        up_pos_height = puzzle[up_pos_row][up_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - up_pos_height), (up_pos_row, up_pos_col), 'DOWN'))


def checkRight(current_pos, pq, puzzle, visited_nodes):
    right_pos_row = current_pos[0]
    right_pos_col = current_pos[1] + 1
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if right_pos_col < len(puzzle[0]) and (right_pos_row, right_pos_col) not in visited_nodes:
        right_pos_height = puzzle[right_pos_row][right_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - right_pos_height), (right_pos_row, right_pos_col), 'LEFT'))


def checkLeft(current_pos, pq, puzzle, visited_nodes):
    left_pos_row = current_pos[0]
    left_pos_col = current_pos[1] - 1
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if left_pos_col >= 0 and (left_pos_row, left_pos_col) not in visited_nodes:
        left_pos_height = puzzle[left_pos_row][left_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - left_pos_height), (left_pos_row, left_pos_col), 'RIGHT'))


def minEffort(puzzle):
    pq = [(0, (0, 0), None)]
    min_effort = 0
    visited_nodes = []

    while True:
        move_effort, current_pos, previous_pos = heapq.heappop(pq)
        if current_pos not in visited_nodes:
            visited_nodes.append(current_pos)
        if move_effort > min_effort:
            min_effort = move_effort

        if len(puzzle) - 1 == current_pos[0] and len(puzzle[0]) - 1 == current_pos[1]:
            return min_effort
        if previous_pos != 'DOWN':
            checkDown(current_pos, pq, puzzle, visited_nodes)
        if previous_pos != 'RIGHT':
            checkRight(current_pos, pq, puzzle, visited_nodes)
        if previous_pos != 'UP':
            checkUp(current_pos, pq, puzzle, visited_nodes)
        if previous_pos != 'LEFT':
            checkLeft(current_pos, pq, puzzle, visited_nodes)



if __name__ == '__main__':
    main()