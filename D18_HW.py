# hw 1
def foo():
    i = 0
    while i < 5:
        yield i
        i += 1


# for j in foo():
#     print(j)

# hw 2
ge = (i for i in range(100) if i % 2 == 0)

for j in (i for i in range(100) if i % 2 == 0):
    print(j)
