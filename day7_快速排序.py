from day2_顺序查找 import *
import random
import copy
import sys
sys.setrecursionlimit(100000)
@cal_time
def fast_sort(list):
    _fast_sort(list, 0, len(list)-1)


def _fast_sort(list, left, right):
    if left < right:
        mid = change_sort(list, left, right)
        _fast_sort(list, left, mid-1)
        _fast_sort(list,mid+1,right)

def change_sort(list, left, right):
    emp = list[left]
    while left < right:
        while list[right] >= emp and left < right:
            right -= 1
        list[left] = list[right]
        while list[left] <= emp and left < right:
            left += 1
        list[right] = list[left]
    list[left] = emp
    return left

@cal_time
def bubble_sort(list):
    num = 0
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        num += 1

a = list(range(0, 10000))
random.shuffle(a)

b = copy.deepcopy(a)
c = copy.deepcopy(a)

fast_sort(b)
bubble_sort(c)

print(b)
print(c)
# a = list(range(99999, 0, -1))
# fast_sort(a)