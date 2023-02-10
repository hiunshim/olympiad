def solve(A, B):
    def f1(L, P, S):
        if L == 0:
            return 1 if P % S == 0 else 0
        return f1(L - 1, P * digit[L], S + digit[L])
    def CountInterestingIntegers(N):
        if N == 0:
            return 0
        count = 0
        for L in range(1, CountDigits(N)):
            count += CountInterestingIntegersWithNumberOfDigits(L)
        count += CountInterestingIntegersWithPrefixOfN(N, P=1, S=0, digit_index=0, is_first_digit=True)
        return count

    def CountInterestingIntegersWithNumberOfDigits(L):
        count = 0
        for digit in range(1, 10):
            count += f1(L - 1, P=digit, S=digit)
        return count

    def CountInterestingIntegersWithPrefixOfN(N, P, S, digit_index, is_first_digit):
        if digit_index == CountDigits(N):
            return 1 if S > 0 and P % S == 0 else 0

        if is_first_digit:
            digit_start = 1
        else:
            digit_start = 0

        count = 0
        for digit in range(digit_start, GetIthDigit(N, digit_index)):
            count += f1(CountDigits(N) - digit_index - 1, P * digit, S + digit)
        count += CountInterestingIntegersWithPrefixOfN(N, P * GetIthDigit(N, digit_index), S + GetIthDigit(N, digit_index), digit_index + 1, is_first_digit=False)
        return count
    return CountInterestingIntegers(B) - CountInterestingIntegers(A - 1)

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        inputs = input().split(' ')
        A = int(inputs[0])
        B = int(inputs[1])
        solution = solve(A, B)
        print(f"Case #{str(tc)}: {solution}")
    

