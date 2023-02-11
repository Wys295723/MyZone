import heapq,random

a = list(range(0, 100))
random.shuffle(a)

heapq.heapify(a)
print(a)

for i in range(len(a)):
    print(heapq.heappop(a), end=',')
