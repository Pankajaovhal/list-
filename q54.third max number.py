n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max1=0
max2=0
max3=0
while i<len(n):
    if n[i]>max1:
        max1=n[i]
    if n[i]>max2 and n[i]!=max1:
        max2=n[i]
    i+=1
i=0
while i<len(n):
    if n[i]>max3 and n[i]!=max2 and n[i]!=max1:
        max3=n[i]
    i+=1
print(max1,max2,max3)


