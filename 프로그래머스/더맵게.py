import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for sco in scoville:
        heapq.heappush(heap,sco)
    cnt = 0
    while True:
        cnt += 1
        if heap:
            a = heapq.heappop(heap)
            if a >= K:
                cnt -= 1
                answer = cnt
                break
        if heap:
            b = heapq.heappop(heap)
            heapq.heappush(heap,a+2*b)
        else:
            answer = -1
            break
    return answer