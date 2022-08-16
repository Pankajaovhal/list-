List=['abc','xyz','aba','1221','cbc']
count=0
for i in List:
#     if len(i) > 1 and i[0] == i[-1]:
    if i[0]==i[-1]:
      count+=1
print(count)



# a=[1,1,2,2,3,1,4,2,3]
# i=0
# count=0
# while i<len(a):
#       a[i]=str(a[i])
#       j=0
#       while j<len(a[i]):
#             if a[i]==a[j]:
#                   count+=1
#             j+=1
#       i+=1
# print(count)


# # a=[1001,1010,100,10]
# # s=[]
# # for i in a:
# #       for j in str(i):
# #             if j=="0":
# #                   pass
# #             else:
# #                   s.append(j)
# # print(s)

                  

        