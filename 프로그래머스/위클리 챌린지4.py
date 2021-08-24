def solution(table, languages, preference):
    answer = ''
    table_dict = {}

    for ta in table:
        a,b,c,d,e,f = ta.split(' ')
        # print(a,b,c,d,e,f)
        table_dict[a] = {b:5, c:4, d:3, e:2, f:1}
    grades = []

    for key,val in table_dict.items():
        grade = 0
        for lang, pre in zip(languages,preference):
            if lang in val:
                grade += pre * table_dict[key][lang]
        grades.append([grade,key])
    # print(grades)
    grades = sorted(grades, key=lambda x:(-x[0],x[1]))
    # print(grades)
    answer = grades[0][1]
    return answer

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7,5,5])
solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"],[7,5])