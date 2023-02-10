import collections
def solve(N, S):
    c = collections.Counter(S)
    for val in c.values():
        if val % 2 == 1:
            return 'IMPOSSIBLE'
    return 'POSSIBLE'

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        S = str(input())
        solution = solve(N, S)
        print(f"Case #{str(tc)}: {solution}")
    

