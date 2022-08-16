# a=[1,2,3,[4,[5,6,[7,8,[9,10],11],12],13],14,15]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     if type(a[i][j][k])==list:
#                         l=0
#                         while l<len(a[i][j][k]):
#                             if type(a[i][j][k][l])==list:
#                                 m=0
#                                 while m<len(a[i][j][k][l]):

#                                     b.append(a[i][j][k][l][m])
#                                     m+=1
#                             else:
#                                 b.append(a[i][j][k][l])
#                             l+=1
#                     else:
#                         b.append(a[i][j][k])
#                     k+=1
#             else:
#                 b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)


# # sum 

# a=[1,2,3,[4,[5,6,[7,8,[9,10],11],12],13],14,15]
# i=0
# b=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     if type(a[i][j][k])==list:
#                         l=0
#                         while l<len(a[i][j][k]):
#                             if type(a[i][j][k][l])==list:
#                                 m=0
#                                 while m<len(a[i][j][k][l]):

#                                     b+=a[i][j][k][l][m]
#                                     m+=1
#                             else:
#                                 b+=a[i][j][k][l]
#                             l+=1
#                     else:
#                         b+=a[i][j][k]
#                     k=k+1
#             else:
#                 b+=a[i][j]
#             j+=1
#     else:
#         b+=a[i]
#     i+=1
# print(b)



# a=[1,2,3,4,5]
# # print(a[0])
# b=15
# a.append(b)
# print(a)
# 2 in a
# print("true")

# a=["red","green","blue","cpn","pink","yellow","black"]
# # b=a[2:6]
# # print(b)
# i=0
# while i<len(a):
#     print(i,a[i])
#     i+=1


a=[1,2,3,[4,[5,6,[7,8,[9,10],11],12],13],14,15]
i=0
while i<len(a):
    i+=1
print(i)








# a=[1,2,3,4,5,3,3,3]
# i=0
# while i<len(a):
#     i+=1
# print(i)




