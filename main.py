import random
import string
from functools import lru_cache
import time

def edit_distance(s1, s2):
    @lru_cache(maxsize=None)
    def d(i,j):
        if i == 0 or j == 0:
            return max(i,j)
        else:
            return min(d(i, j-1) + 1,
                       d(i-1, j) + 1,
                       d(i-1, j-1) + (s1[i-1] != s2[i-1]))
    return d(len(s1), len(s2))

def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))

def test(n_iter = 100):
    for i in range(n_iter):
        length = random.randint(0, 64)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        assert edit_distance(s, '') == edit_distance('', s) == len(s)
        assert edit_distance(s,s) == 0
    # assert edit_distance('distance', 'editing') == 5
    assert edit_distance('hello', 'mello') == 1

if __name__ == '__main__':
    for i in range(10):
        start = time.time()
        test(1000)
        end = time.time()
        print(end-start)
