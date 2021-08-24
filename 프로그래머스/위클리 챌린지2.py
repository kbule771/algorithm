def solution(scores):
    answer = ''
    for i in range(len(scores)):
        my_grades = []
        my_grade = scores[i][i]
        for j in range(len(scores)):
            my_grades.append(scores[j][i])
        min_c = 0
        max_c = 0
        minnum = min(my_grades)
        maxnum = max(my_grades)
        flag = 0
        if my_grade == minnum:
            flag = 1
        elif my_grade == maxnum:
            flag = 2

        for mg in my_grades:
            if mg == minnum:
                min_c += 1
            if mg == maxnum:
                max_c += 1
        # print(flag, min_c,max_c)
        if min_c == 1 and flag == 1:
            avg = (sum(my_grades) - my_grade) / (len(scores)-1)
        elif max_c == 1 and flag == 2:
            avg = (sum(my_grades) - my_grade) / (len(scores)-1)
        else:
            avg = sum(my_grades) / len(scores)
            
        # print(avg)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))