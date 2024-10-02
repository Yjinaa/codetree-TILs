n = int(input())

ns = [str(input()) for _ in range(n)]

max_val = 0
at_least = False
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            max_len = max(len(ns[i]), len(ns[j]), len(ns[k]))
            # n1 = [int(char) for char in list(str(ns[i].zfill(max_len)))]
            # n2 = [int(char) for char in list(str(ns[j].zfill(max_len)))]
            # n3 = [int(char) for char in list(str(ns[k].zfill(max_len)))]
            n1 = ns[i].zfill(max_len)
            n2 = ns[j].zfill(max_len)
            n3 = ns[k].zfill(max_len)
            answer = '0'
            for l in range(max_len):
                if int(n1[l]) + int(n2[l]) + int(n3[l]) < 10:
                    answer += str(int(n1[l]) + int(n2[l]) + int(n3[l]))
                    continue
                else:
                    break
            if len(str(int(answer))) == max_len:
                at_least = True
                if int(answer) > max_val:
                    max_val = int(answer)

if at_least == False:
    print(-1)
else:
    print(max_val)