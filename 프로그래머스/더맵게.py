import heapq

li = [4,3,1,5]

heap = heapq.heapify(li)
for i in range(4):
    a = heapq.heappop(li)
    print(a)