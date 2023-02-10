def solve(I, P):
    N = len(I)
    M = len(P)
    ptrI = 0
    ptrP = 0
    while ptrI < N and ptrP < M:
        if I[ptrI] == P[ptrP]:
            ptrI += 1
            ptrP += 1
        else:
            ptrP += 1
    if ptrI == N:
        return str(M - N)
    else:
        return 'IMPOSSBILE'

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        I = input()
        P = input()
        solution = solve(I, P)
        print("Case #%d: %s" % (tc, solution))
    

