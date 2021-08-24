def solution(money):
    answer = 0
    dp1 = [0]*len(money)
    dp2 = [0]*len(money)
    # 0부터 시작한 경우
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2,len(money)-1):
        dp1[i] = max(dp1[i-2] + money[i],dp1[i-1])
    # 1부터 시작한 경우
    dp2[1] = money[1]
    for i in range(2,len(money)):
        dp2[i] = max(dp2[i-2] + money[i],dp2[i-1])
        
        


    # print(dp1)
    # print(dp2)
        
    answer = max(max(dp1),max(dp2))
    # print(answer)   

    return answer

solution([1,2,3,1])