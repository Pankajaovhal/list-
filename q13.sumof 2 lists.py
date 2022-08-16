a=[1,2,3]
b=[3,2,1]
i=0
sum=1
s2=1
s3=0
while i<len(a):
    if type(a[i])==int:
        sum=sum*b[i]
        s2=s2*a[i]
        s3=sum*s2
    i+=1
print(s3)


