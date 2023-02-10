from typing import Set

from test_framework import generic_test

import collections
import string

def transform_string(D: Set[str], s: str, t: str) -> int:
    # TODO - you fill in here.
    StringWithDistance = collections.namedtuple('StringWithDistance',
        ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    while q:
        f = q.popleft()
        if f.candidate_string == t:
            return f.distance
        for i in range(len(s)):
            for c in string.ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
