import random
import string
import time

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    if m < n:
        return edit_distance(s2, s1)

    previous = list(range(n+1))

    for i, char1 in enumerate(s1, 1):
        current = [i]
        for j, char2 in enumerate(s2, 1):
            current.append(min(current[j-1] + 1,
                                previous[j] + 1,
                                previous[j-1] + (char1 != char2)))
        previous = current

    return previous[n]

def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))

def test(n_iter = 100):
    for i in range(n_iter):
        length = random.randint(0, 64)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        assert edit_distance(s, '') == edit_distance('', s) == len(s)
        assert edit_distance(s, s) == 0
    assert edit_distance('distance', 'editing') == 5
    assert edit_distance('hello', 'mello') == 1

if __name__ == '__main__':
    for i in range(10):
        start = time.time()
        test(1000)
        end = time.time()
        print(end-start)