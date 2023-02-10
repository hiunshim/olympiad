import sys

def create_indegree(N, F_i, P_i):
    indegree = [0 for _ in range(N + 1)]
    for module in P_i:
        indegree[module] += 1
    return indegree

def dfs(module, F_i, P_i):
    if module == 0:
        return 0
    res = max(F_i[module], dfs(P_i[module], F_i, P_i))
    P_i[module] = 0
    F_i[module] = 0
    return res

def trigger(zero_indegrees, F_i, P_i):
    F_copy = [x for x in F_i]
    P_copy = [x for x in P_i]
    return sum(dfs(module, F_copy, P_copy) for module in zero_indegrees)

def solve(N, F_i, P_i):
    indegree = create_indegree(N, F_i, P_i)
    zero_indegrees = [i for i in range(len(indegree)) if indegree[i] == 0]
    def permutate(i):
        nonlocal ans
        if i == len(zero_indegrees):
            ans = max(ans, trigger(zero_indegrees.copy(), F_i, P_i))
            return
        for j in range(i, len(zero_indegrees)):
            zero_indegrees[i], zero_indegrees[j] = zero_indegrees[j], zero_indegrees[i]
            permutate(i + 1)
            zero_indegrees[i], zero_indegrees[j] = zero_indegrees[j], zero_indegrees[i]
    ans = 0
    permutate(0)
    return ans
            

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        F_i = [0] + list(map(int, sys.stdin.readline().strip().split()))
        P_i = [0] + list(map(int, sys.stdin.readline().strip().split()))
        ans = solve(N, F_i, P_i)
        print(f"Case #{test_case}: {ans}")

if __name__ == "__main__":
    main()

