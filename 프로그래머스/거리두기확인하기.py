def solution(places):
    answer = []
    # 가로세로 방향 확인
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    # 대각방향 확인
    dx1 = [1,-1,1,-1]
    dy1 = [1,1,-1,-1]
    for place in places:
        ans = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    for k in range(4):
                        I = dx[k] + i
                        J = dy[k] + j
                        if 0 <= I <=4 and 0 <= J <=4 and place[I][J] == "P":
                            ans = 0
                            answer.append(ans)
                            break


                if place[i][j] == "O":
                    count = 0
                    for k in range(4):
                        I = dx[k] + i
                        J = dy[k] + j
                        if 0 <= I <=4 and 0 <= J <=4 and place[I][J] == "P":
                            count += 1
                        if count == 2:
                            ans = 0
                            answer.append(ans)
                            break
                if ans == 0:
                    break
            if ans == 0:
                break
        if ans == 1:
            answer.append(ans)

    return answer