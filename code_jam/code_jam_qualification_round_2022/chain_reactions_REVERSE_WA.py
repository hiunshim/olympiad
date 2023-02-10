import sys
import collections

def create_indegree(N, F, P):
    indegree = [0 for _ in range(N + 1)]
    for module in P:
        indegree[module] += 1
    return indegree

def create_graph(N, F, P):
    adj_list = collections.defaultdict(list)
    for i, module in enumerate(P):
        adj_list[module].append(i)
    return adj_list

def solve(N, F, P):
    def get_min(module):
        if not graph[module]:
            minimum_fun[module] = F[module]
        for next_module in graph[module]:
            if next_module != module:
                minimum_fun[module] = min(minimum_fun[module], F[module] + get_min(next_module))
        return minimum_fun[module]

    def dfs(module, fun):
        if visited[module] != WHITE:
            return
        if not graph[module]:
            F[module] = max(fun, F[module])
        visited[module] = GRAY
        least_fun = float('inf')
        least_fun_module = None
        for next_module in graph[module]:
            if minimum_fun[next_module] < least_fun:
                least_fun = minimum_fun[next_module]
                least_fun_module = next_module
        for next_module in graph[module]: 
            if next_module == least_fun_module:
                dfs(next_module, F[module])
            else:
                dfs(next_module, 0)
        visited[module] = BLACK

    graph = create_graph(N, F, P)
    indegree = create_indegree(N, F, P)
    minimum_fun = [float('inf') for _ in range(N + 1)]
    zero_indegrees = [i for i in range(len(indegree)) if indegree[i] == 0]
    WHITE, GRAY, BLACK = 0, 1, 2
    visited = [WHITE for _ in range(N + 1)]
    get_min(0)
    dfs(0, 0)
    return sum(F[i] for i in zero_indegrees)

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        F = [0] + list(map(int, sys.stdin.readline().strip().split()))
        P = [0] + list(map(int, sys.stdin.readline().strip().split()))
        ans = solve(N, F, P)
        print(f"Case #{test_case}: {ans}")

if __name__ == "__main__":
    main()


