def select_sort(args):
    for i in range(len(args)-1):
        min_loc = i
        for j in range(i, len(args)):
            if args[j] < args[min_loc]:
                min_loc = j
        args[i], args[min_loc] = args[min_loc], args[i]
    return args


a = [2, 1, 6, 5, 9, 8, 3, 7, 4]
print(select_sort(a))