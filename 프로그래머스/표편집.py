def solution(n, k, cmd):
    answer = ''
    data={}
    for i in range(n):
        data[i] = 'O'
    print(data)
    record = []
    for c in cmd:
        if len(c) > 1:
            c1,c2 = c.split(' ')
            c2 = int(c2)
        else:
            c1 = c
        if c1 == 'D':
            cnt = 0
            d = 0
            while cnt < c2:
                d += 1
                if data[k+d] == 'O':
                    cnt += 1
            k = k + d
            if k > n:
                k = n
        elif c1 == 'U':
            print('here',k)
            cnt = 0
            u = 0
            while cnt < c2:
                u += 1
                if data[k-u] == 'O':
                    cnt += 1
            k = k - u
            if k <0:
                k = 0
            print(k)
        elif c1 == 'C':
            record.append(k)
            data[k] = 'X'
            p, q = k, k
            flag = 0
            while p < n :
                p += 1
                if p in data and data[p] == 'O':
                    k = p
                    flag = 1
                    break
            if flag == 0:
                while q>=0 :
                    q -= 1
                    if q in data and data[q] == 'O':
                        k = q
                        break
        else:
            tmp = record.pop()
            data[tmp] = 'O'
        print(data,k,c,record)
    for val in data.values():
        answer += val
    print(answer)
    return answer
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])