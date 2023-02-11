from day2_顺序查找 import *

@cal_time
def binary_search(list, num):
    t1 = time.time()
    print(t1)
    left = 0
    right = len(list) - 1
    while right > left:
        mid = (left + right) // 2
        if list[mid] == num:
            print(time.time())
            return mid
        elif list[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return None

a =list(range(1000000))
binary_search(a, 285955)
print(time.time())