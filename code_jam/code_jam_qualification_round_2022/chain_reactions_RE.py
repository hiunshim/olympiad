import sys
import collections

def create_graph(N, F, P):
    adj_list = collections.defaultdict(list)
    for i in range(N):
        adj_list[P[i]].append(i + 1)
    return adj_list

def solve(N, F, P):
    def dfs(module):
        if not graph[module]:
            return F[module - 1]
        funs = [dfs(next_module) for next_module in graph[module]]
        min_fun = min(funs)
        nonlocal ans
        ans += (sum(funs) - min_fun)
        return max(min_fun, F[module - 1])
    graph = create_graph(N, F, P)
    ans = 0
    for module in graph[0]:
        ret = dfs(module)
        ans += ret
    return ans

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        F = list(map(int, sys.stdin.readline().strip().split()))
        P = list(map(int, sys.stdin.readline().strip().split()))
        ans = solve(N, F, P)
        print(f"Case #{test_case}: {ans}")

if __name__ == "__main__":
    main()

