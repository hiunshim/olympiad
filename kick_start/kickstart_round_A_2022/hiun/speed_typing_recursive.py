def solve(P, I):
    def lcs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(P):
            return 0
        if j == len(I):
            return 0
        if P[i] == I[j]:
            memo[(i, j)] = 1 + lcs(i + 1, j + 1)
            return memo[(i, j)] 
        memo[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
        return memo[(i, j)]
    memo = {}
    subsequence = lcs(0, 0)
    if subsequence < len(P):
        return 'IMPOSSIBLE'
    to_delete = len(I) - subsequence
    return str(to_delete)

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        str1 = input().strip()
        str2 = input().strip()
        solution = solve(str(str1), str(str2))
        print("Case #%d: %s" % (tc, solve(str1, str2)))
    
