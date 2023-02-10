def solve(digits):
    L = len(digits)
    num = 0
    for digit in digits:
        num += int(digit)
    d = 9 - (num % 9)
    if d == 9:
        return digits[0:1] + '0' + digits[1:] 
    i = 0
    while i < L and d >= int(digits[i]):
        i += 1
    return digits[:i] + str(d) + digits[i:]

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        x = str(input())
        solution = solve(x)
        print(f"Case #{str(tc)}: {solution}")
    
