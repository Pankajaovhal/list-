# n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# mx=max(n[0],n[1])
# smx=min(n[0],n[1])
# l=len(n)
# i=0
# while i<l:
#     if n[i]>mx:
#         smx=mx
#         mx=n[i]
#     elif n[i]>smx and mx!=n[i]:
#         smx=n[i]
#     i+=1
# print("second highest number is :",str(smx))


# n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=len(n[0:1])
# min=len(n[0:1])
# mx=max
# smx=min
# l=len(n)
# i=0
# while i<l:
#     if n[i]>mx:
#         smx=mx
#         mx=n[i]
#     elif n[i]>smx and mx!=n[i]:
#         smx=n[i]
#     i+=1
# print("second highest number is :",str(smx))


# print(sorted(n)(-2))

# n.sort()
# print(n[-2])


n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
max=len(n[0:1])
min=len(n[0:1])
d=len(n[0:1])
mx=max
smx=min
tmx=d
l=len(n)
i=0
while i<l:
    if n[i]>mx:
        smx=mx
        mx=n[i]
    if n[i]>smx and mx!=n[i]:
        smx=n[i]
    if n[i]>tmx and n[i]!=smx and n[i]!=mx:
        tmx=n[i]
    i+=1
print("frist max number:",str(mx))
print("second max number is :",str(smx))
print("thrid max number:",str(tmx))

