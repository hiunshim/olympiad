import sys

def solve(N, S_i):
    S_i.sort()
    count = 0
    for s in S_i:
        if s > count:
            count += 1
    return min(N, count)
    
def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        S_i = list(map(int, sys.stdin.readline().strip().split()))
        solution = solve(N, S_i)
        print(f"Case #{test_case}: {solution}")

if __name__ == "__main__":
    main()

