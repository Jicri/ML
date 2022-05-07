# hw 1
def foo1():
    var1 = 0

    def foo2():
        nonlocal var1
        print(var1)
        var1 = 1  # 修改局部變數值
    foo2()


foo1()

# hw 2
a = "A"
z = 1


def f(b):
    a = "AAA"
    c = "C"
    print(a)
    print(b)
    print(c)
    return b

# print(a)->A
# print('B')-> AAA B c B
# print(a)->A
