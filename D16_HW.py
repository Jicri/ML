# Map 四捨五入
from functools import reduce


def rounding(x):
    x = str(x)
    x = x.split('.')
    for i in range(len(x)):
        if i > 0 and int(x[i]) < 5:
            a = int(x[0])
            return a
        elif i > 0 and int(x[i]) >= 5:
            b = int(x[0]) + 1
            return b


L1 = [1.2, 4.5, 2.3, 2.9, 8.7]

# print(list(map(rounding, L1)))

# filter > 30
L2 = [1, 2, 40, 50, 25, 12]
# print(list(filter(lambda x: x > 30, L2)))

# reduce
L3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: x+y, L3))

# isPrime map()


def isPrime(x):
    count = 0
    for i in range(1, x+1):
        if x != i and x % i != 0:
            count += 1
        elif x != i and x % i == 0:
            count == 0
    if count == x-2:
        return True
    else:
        return False


L4 = [2, 3, 4, 5, 6, 7, 10, 23]

print(list(map(isPrime, L4)))
