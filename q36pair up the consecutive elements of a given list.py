a=[1,2,3,4,5,6,7]
i=0
b=[]
while i<1:
    j=0
    k=j+1
    while j<len(a) and k<len(a):
        b.append([a[j],a[k]])
        j=j+1
        k=k+1
    i=i+1
print(b)
    
