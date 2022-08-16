a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
k=4
i=0
list=[]
while i<len(a):
    if i==k:
        list.append(20)
        k+=4
    list.append(a[i])
    i+=1
print(list)
