# a=[1,2,3,4,5,6,7,8,9,10]
# b=a[2:-7]
# c=a[5:-4]
# d=a[7:]
# print()


a=[[1,3,2],[4,10,6],[7,11,9]]
i=0
# max=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        max=a[i][j]
        while j<len(a[i]):
            if a[i][j]<max:
                max=a[i][j]
            j+=1
        i+=1
    b.append(max)
print(b)
# print(max)