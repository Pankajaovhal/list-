a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# i=0
# while i<len(a):
#     if a[i]>0:
#         d=a[i]**2
#     i+=1
# print(d[:5])
# print(d[-5:])


l = list()
for i in range(1,21):
    l.append(i**2)
print(l[:5])
print(l[-5:])