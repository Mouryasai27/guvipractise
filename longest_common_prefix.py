def prefix(st1,st2):
    l1 = len(st1)
    l2 = len(st2)
    result = ""
    i = 0
    j = 0
    while(i <= l1-1 and j <= l2-1):
        if (st1[i] != st2[i]):
            break
        result += (st1[i])
        i += 1
        j += 1

    return (result)

def sort(a,n):
    a.sort(reverse = False)
    print(prefix(a[0],a[n-1]))


n = int(input())
a = []
for i in range(n):
    x = input()
    a.append(x)
sort(a,n)
