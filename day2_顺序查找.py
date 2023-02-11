import time
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print("%s程序消耗时长:%s" % (func.__name__, t2 - t1))
        return result
    return wrapper

@cal_time
def linear_search(list, num):
    for index, var in enumerate(list):
        if var == num:
            return index
    else:
        return None


a = [1, 5, 7, 9, 11, 15, 0, 3, 2]