# Caleb Verstraete
# 2/23/23
# CS325
import heapq


def main():
    print(minEffort([[1, 3, 5],
                     [2, 8, 9],
                     [4, 4, 5]]))


def checkDown(current_pos, pq, puzzle):
    down_pos_row = current_pos[0] + 1
    down_pos_col = current_pos[1]
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if down_pos_row < len(puzzle):
        down_pos_height = puzzle[down_pos_row][down_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - down_pos_height), (down_pos_row, down_pos_col), 'UP'))


def checkUp(current_pos, pq, puzzle):
    up_pos_row = current_pos[0] - 1
    up_pos_col = current_pos[1]
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if up_pos_row >= 0:
        up_pos_height = puzzle[up_pos_row][up_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - up_pos_height), (up_pos_row, up_pos_col), 'DOWN'))


def checkRight(current_pos, pq, puzzle):
    right_pos_row = current_pos[0]
    right_pos_col = current_pos[1] + 1
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if right_pos_col < len(puzzle[0]):
        right_pos_height = puzzle[right_pos_row][right_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - right_pos_height), (right_pos_row, right_pos_col), 'LEFT'))


def checkLeft(current_pos, pq, puzzle):
    left_pos_row = current_pos[0]
    left_pos_col = current_pos[1] - 1
    current_pos_height = puzzle[current_pos[0]][current_pos[1]]
    if left_pos_col >= 0:
        left_pos_height = puzzle[left_pos_row][left_pos_col]
        heapq.heappush(pq, (abs(current_pos_height - left_pos_height), (left_pos_row, left_pos_col), 'RIGHT'))


def minEffort(puzzle):
    pq = [(0, (0, 0), None)]
    min_effort = 0

    while True:
        move_effort, current_pos, previous_pos = heapq.heappop(pq)
        if move_effort > min_effort:
            min_effort = move_effort

        if len(puzzle) - 1 == current_pos[0] and len(puzzle[0]) - 1 == current_pos[1]:
            return min_effort
        if previous_pos != 'DOWN':
            checkDown(current_pos, pq, puzzle)
        if previous_pos != 'RIGHT':
            checkRight(current_pos, pq, puzzle)
        if previous_pos != 'UP':
            checkUp(current_pos, pq, puzzle)
        if previous_pos != 'LEFT':
            checkLeft(current_pos, pq, puzzle)


if __name__ == '__main__':
    main()