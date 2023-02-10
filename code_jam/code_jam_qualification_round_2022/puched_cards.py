import sys

def print_first_three_lines(c):
    first_line = "..+" + "-+" * (c - 1)
    second_line = "..|" + ".|" * (c - 1)
    third_line = "+-+" + "-+" * (c - 1)
    print(first_line)
    print(second_line)
    print(third_line)

def print_row(r, c):
    while r:
        print("|" + ".|" * c) 
        print("+" + "-+" * c)
        r -= 1

def main():
    T = int(input())
    for tc in range(1, T + 1):
        r, c = map(int, sys.stdin.readline().strip().split())
        print(f"Case #{tc}:")
        print_first_three_lines(c)
        print_row(r - 1, c)

if __name__ == '__main__':
    main()

