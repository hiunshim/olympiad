import collections

def solve(P, I):
    if P == I:
        return '0'
    if len(P) > len(I):
        return 'IMPOSSIBLE'
    c1 = collections.Counter(P)
    c2 = collections.Counter(I)
    for c in P:
        if c1[c] > c2[c]:
            return 'IMPOSSIBLE'
    dp = [[0 for _ in range(len(P) + 1)] for _ in range(2)]
    for i in range(len(I)):
        for j in range(len(P)):
            if I[i] == P[j]:
                dp[1 - i % 2][j + 1] = dp[i % 2][j] + 1
            else:
                dp[1 - i % 2][j + 1] = max(dp[1 - i % 2][j], dp[i % 2][j + 1])
            if dp[1 - i % 2][j + 1] == len(P):
                return str(len(I) - len(P))
    subsequence = dp[len(I) % 2][len(P)]
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
    
