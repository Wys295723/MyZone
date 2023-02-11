def merge(list, left, mid, right):
    i = left
    j = mid + 1
    tmp = []
    while i <= mid and j <= right:
        if list[i] < list[j]:
            tmp.append(list[i])
            i += 1
        else:
            tmp.append(list[j])
            j += 1
    while i <= mid:
        tmp.append(list[i])
        i += 1
    while j <= right:
        tmp.append(list[j])
        j += 1
    list[left:right+1] = tmp

def merge_sort(list, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(list, left, mid)
        merge_sort(list, mid + 1, right)
        merge(list, left, mid, right)

a = list(range(0, 100))
import random
random.shuffle(a)

merge_sort(a, 0, len(a)-1)
print(a)