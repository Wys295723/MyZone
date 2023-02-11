def insert_sort(list):
    for i in range(1, len(list)):
        emp = list[i]
        j = i - 1
        while j >= 0 and list[j] > emp:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = emp


a = [2, 1, 6, 5, 9, 8, 3, 7, 4]
insert_sort(a)
print(a)
