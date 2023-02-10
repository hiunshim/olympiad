from copy import deepcopy

DIRECTIONS = ((0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1))

def flood(board, row, col, n, color):
    board[row][col] = color.lower()
    for direction in DIRECTIONS:
        new_row, new_col = row + direction[0], col + direction[1]
        if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n and board[new_row][new_col] == color:
            flood(board, new_row, new_col, n, color)

def check_winner(board, n):
    for i in range(n):
        if board[i][0] == 'B':
            flood(board, i, 0, n, 'B')
        if board[0][i] == 'R':
            flood(board, 0, i, n, 'R')
    for i in range(n):
        if board[i][n - 1] == 'b':
            return 'B'
        if board[n - 1][i] == 'r':
            return 'R'
    return '.'

def count_stones(board):
    num_red, num_blue = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                num_red += 1
            if board[i][j] == 'B':
                num_blue += 1
    return num_red, num_blue

def solve(original_board, n):
    num_red, num_blue = count_stones(original_board)
    if abs(num_red - num_blue) > 1:
        return 'Impossible'
    board = deepcopy(original_board)
    winner = check_winner(board, n)
    if winner == '.':
        return 'Nobody wins'
    if (winner == 'B' and num_blue < num_red) or (winner == 'R' and num_red < num_blue):
        return 'Impossible'

    # cut the connection one by one and see if they're still connected
    for row in range(n):
        for col in range(n):
            if original_board[row][col] == winner:
                board = deepcopy(original_board)
                board[row][col] = '.'
                if check_winner(board, n) == '.':
                    if winner == 'B':
                        return 'Blue wins'
                    if winner == 'R':
                        return 'Red wins'
    return 'Impossible'


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        board_size = int(input())
        board = []
        for _ in range(board_size):
            board.append(list(input()))
        ans = solve(board, board_size)
        print(f"Case #{test_case}: {ans}")


if __name__ == "__main__":
    main()

