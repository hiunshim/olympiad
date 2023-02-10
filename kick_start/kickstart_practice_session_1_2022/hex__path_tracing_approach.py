DIRECTIONS = ((0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1))

def get_next_hex(left, right):
    right_dir = (right[0] - left[0], right[1] - left[1])
    for index, direction in enumerate(DIRECTIONS):
        if right_dir == direction:
            next_dir = DIRECTIONS[(index + 1) % 6]
            return (left[0] + next_dir[0], left[1] + next_dir[1])

def step(padded_board, color, left, right):
    next_hex = get_next_hex(left, right)
    if padded_board[next_hex[0]][next_hex[1]] == color:
        return next_hex, right
    else:
        return left, next_hex

def blue_path_south(padded_board, m):
    left, right = (m - 1, 0), (m - 1, 1) # blue starting bottom left and red starting bottom right
    path = set()
    while left[1] < m - 1: # while haven't reached east
        path.add(left)
        left, right = step(padded_board, 'B', left, right)
        if right[0] == 0: # if reached the top
            return None
    return path
def blue_path_north(padded_board, m):
    left, right = (0, 0), (0, 1)
    path = set()
    while left[1] < m - 1:
        path.add(left)
        left, right = step(padded_board, 'B', left, right)
        if right[0] == m - 1:
            return None
    return path
def red_path_west(padded_board, m):
    left, right = (0, 0), (0, 1)
    path = set()
    while right[1] < m - 1:
        path.add(left)
        left, right = step(padded_board, 'R', left, right)
        if right[0] == m - 1:
            return None
    return path
def red_path_east(padded_board, m):
    left, right = (m - 1, 0), (m - 1, 1)
    path = set()
    while right[1] < m - 1:
        path.add(left)
        left, right = step(padded_board, 'R', left, right)
        if right[0] == 0:
            return None
    return path

def count_stones(board):
    num_red, num_blue = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'B':
                num_blue += 1
            if board[i][j] == 'R':
                num_red += 1
    return num_red, num_blue

def pad_board(board, n):
    new_board = []
    for i in range(n):
        new_board.append(['B'] + board[i] + ['B'])
    new_board = ['R' for _ in range(n)] + new_board + ['R' for _ in range(n)]
    return new_board 

def solve(board, n):
    num_red, num_blue = count_stones(board)
    if abs(num_red - num_blue) > 1:
        return 'Impossible'
    
    padded_board = pad_board(board, n)
    m = n + 2
    
    south_path = blue_path_south(padded_board, m)
    if south_path:
        north_path = blue_path_north(padded_board, m)
        common_blue_stones = south_path.intersection(north_path)
        if common_blue_stones and num_blue >= num_red:
            return 'Blue wins'
        else:
            return 'Impossible'

    west_path = red_path_west(padded_board, m)
    if west_path:
        east_path = red_path_east(padded_board, m)
        common_red_stones = west_path.intersection(east_path)
        if common_red_stones and num_red >= num_blue:
            return 'Red wins'
        else:
            return 'Impossible'

    return 'Nobody wins'

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

