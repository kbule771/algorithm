def solution(progresses, speeds):
    left_day = []
    for i in range(len(progresses)):
        
        if ((100-progresses[i]) /speeds[i]) == (100-progresses[i]) //speeds[i]: #나누어 떨어짐
            left_day.append(int((100-progresses[i]) /speeds[i]))
        else:
            left_day.append(((100-progresses[i]) //speeds[i])+ 1)
    result = []
    tmp = left_day[0]
    count = 1
    for i in range(1,len(left_day)):
        if left_day[i]<=tmp:
            count += 1
        else:
            tmp = left_day[i]
            result.append(count)
            count = 1
    result.append(count)
    return result