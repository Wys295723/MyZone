import random
def bubble_sort(list):
    num = 0
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        print(num, "--", list)
        num += 1
    return list


a = [2, 1, 6, 5, 9, 8, 3, 7, 4]
b = [random.randint(0, 1000) for i in range(1000)]
bubble_sort(b)