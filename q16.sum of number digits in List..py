a=[12,67,98,34]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    c=str(a[i])
    while j<len(c):
        sum+=int(c[j])
        j+=1
    b.append(sum)
    i+=1
print(b)
