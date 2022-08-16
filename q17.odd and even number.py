# l=[34,222,2,4,6,5,7,89,43,65,72,84]
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         print(l[i],"even number")
#     else:
#         print(l[i],"odd number")
#     i+=1



# l=[34,22,2,4,6,5,7,89,43,65,72,84]
# en=[]
# on=[]
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         en.append(l[i])
#     else:
#         on.append(l[i])  
#     i+=1
# print("odd number:",on)  
# print("even number:",en)

a=[5,2,0,1,10,9,7,3]
b=[]
k=[]
i=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    else:
        k.append(a[i])
    i+=1
b.extend(k)
print(b)
