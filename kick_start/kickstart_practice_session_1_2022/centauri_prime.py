VOWELS = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    # TODO: Add logic to determine the ruler of the kingdom
    # It should be either 'Alice', 'Bob' or 'nobody'.
    ruler = ''
    last_letter = kingdom[-1]
    if last_letter == 'y' or last_letter == 'Y':
        ruler = 'nobody'
    elif last_letter in VOWELS:
        ruler = 'Alice'
    else:
        ruler = 'Bob'
    return ruler

def main():
    # Get the number of test cases
    T = int(input())
    for t in range(T):
        # Get the kingdom
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
    main()
