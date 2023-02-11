import time
def hanoi(n, a, b, c):
    """
    汉诺塔问题
    :param n: 一共有打多少个盘子
    :param a: 第一个柱子
    :param b: 第二个柱子
    :param c: 第三个柱子
    """
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n - 1, b, a, c)

print(time.time())
hanoi(5, "A", "B", "C")
print(time.time())