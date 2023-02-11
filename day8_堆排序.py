from day2_顺序查找 import *


def sift(list, first, end):
    emp = list[first]
    i = first
    j = 2 * i + 1
    while j <= end:
        if j + 1 <= end and list[j + 1] > list[j] :
            # 必须
            j = j + 1
        if list[j] > emp:
            list[i] = list[j]
            i = j
            j = 2*i + 1
        else:
            list[i] = emp
            break
    else:
        list[i] = emp

@cal_time
def heap_sort(list):
    end = len(list) - 1
    for i in range((end-1)//2, -1, -1):
        sift(list, i, end)
    for i in range(end, -1, -1):
        list[0], list[i] = list[i], list[0]
        sift(list, 0, i - 1)


a = [i for i in range(10000)]
import random
random.shuffle(a)
print(a)
heap_sort(a)
print(a)
