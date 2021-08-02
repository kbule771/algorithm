def solution(clothes):
    
    data = {}
    
    for clothe in clothes:
        if clothe[1] in data:
            data[clothe[1]].append(clothe[0])
        else:
            data[clothe[1]] = [clothe[0]]

    number = 1
    for value in data.values():
        number *= (len(value)+1)

    
    answer = number -1
    return answer