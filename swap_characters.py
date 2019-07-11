n = list(input())
li = []
for i in range(0,len(n),2):
    temp = n[i]
    n[i] = n[i+1]
    n[i+1] = temp
    li.append(n[i])
    li.append(n[i+1])
print("".join(li))
