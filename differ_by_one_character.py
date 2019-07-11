a,b = list(input().split())
diff = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            diff += 1
if diff == 1:
    print("yes")
else:
    print("no")
