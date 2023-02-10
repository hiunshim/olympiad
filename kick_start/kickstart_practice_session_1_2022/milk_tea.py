class ScoredTea:
    def __init__(self, score, tea):
        self.score = score
        self.tea = tea
    def compare(self, o):
        return self.score - o.score

def compare(prefix, tea):
    difference = 0
    for i in range(len(prefix)):
        if prefix[i] != tea[i]:
            difference += 1
    return difference

def score(prefix, teas):
    difference = 0
    for tea in teas:
        difference += compare(prefix, tea)
    return difference

def expand(lst, prefix, teas):
    zero = prefix + '0'
    lst.append(ScoredTea(score(zero, teas), zero))
    one = prefix + '1'
    lst.append(ScoredTea(score(one, teas), zero))

def count_complaints(preferences, forbiddens):
    complaints = 0
    return complaints

if __name__ == '__main__':
    num_cases = int(input())
    for tc in range(1, num_cases + 1):
        num_friends, num_forbidden, num_options = map(int, input().split())
        preferences = [input() for _ in range(num_friends)]
        forbiddens = [input() for _ in range(num_forbidden)]
        print("Case #%d: %d" % (tc, count_complaints(preferences, forbiddens)))

