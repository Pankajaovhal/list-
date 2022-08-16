n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
sum=0
l=len(n)
while i<l:
    m=n[i]
    if m>sum:
        sum=m
    i+=1
print(sum)


# print(max(n))