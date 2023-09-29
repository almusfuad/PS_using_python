from collections import Counter

n = int(input())
arr = list(map(int, input().split()))


count = Counter(arr)
removals = 0


for x in count:
    if x <= n:
        if count[x] > x:
            removals = count[x] - x
        elif count[x] < x:
            removals = x - count[x]
    else:
        removals = n

print(removals)