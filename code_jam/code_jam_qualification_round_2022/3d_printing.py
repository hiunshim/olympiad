import sys

def solve(printer_1, printer_2, printer_3):
    colors = [min(printer_1[i], printer_2[i], printer_3[i]) for i in range(4)]
    if sum(colors) < 10 ** 6:
        return "IMPOSSIBLE"
    remainder = sum(colors) - (10 ** 6)
    for i in range(4):
        if remainder == 0:
            return " ".join(map(str, colors))
        remainder -= colors[i]
        colors[i] = 0
        if remainder < 0:
            colors[i] -= remainder
            remainder = 0
    return "IMPOSSIBLE"




def main():
    T = int(input())
    for test_case in range(1, T + 1):
        printer_1 = list(map(int, sys.stdin.readline().strip().split()))
        printer_2 = list(map(int, sys.stdin.readline().strip().split()))
        printer_3 = list(map(int, sys.stdin.readline().strip().split()))
        color = solve(printer_1, printer_2, printer_3)
        print(f"Case #{test_case}: {color}")

if __name__ == "__main__":
    main()

