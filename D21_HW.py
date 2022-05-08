import unittest
import pdb

c = 2
a = 1
print(a)
pdb.set_trace()
print(c)


def f1():
    L = []
    for num in range(1, 100 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                L.append(num)
    return L


def f2():
    return [x for x in range(1, 101) if x > 1 if x not in [j for i in range(2, 11) for j in range(2*i, 101, i)]]


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def test_f1(self):
        self.assertEqual(f1(), self.ans)

    def test_f2(self):
        self.assertEqual(f2(), self.ans)


unittest.main(argv=[''], verbosity=2, exit=False)
