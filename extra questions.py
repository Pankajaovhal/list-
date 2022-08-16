# # 1 make a flat list.
# a=[1,2,3,4,5,[6,7,8],[8,2,2]]
# b=[]
# i=0
# while i<len(a):
#     # print(a[i])
#     if type(a[i]) is list:
#         j=0
#         while j <len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#         i+=1
# print(b)




# # 2
# a=[1,3,5,7,8,10]
# i=1
# while i<=10:
#     if i not in a:
#         print(i)
#     i+=1



# # 3
# list=["q","z"]
# num=int(input("enter your number: "))
# i=1
# while i<=num:
#     j=1
#     while j<num:
#         j+=1
# print( '"' +"q",str(i), '"','"' +"z",str(i),'"')
# print()
# i+=1


# # 4 make a flat list.
# list=[5,6,[],3,[],[],9]
# i=0
# a=[]
# while i<len(list):
#     if list[i]!=[]:
#         a.append(list[i])
#     i+=1
# print(a)



# # 5 make a flat list.
# list=[5,6,[],3,[],[],9]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==int:
#         a.append(list[i])
#     i+=1
# print(a)




# # 6
# list=[["g","f","g"],["i","s"],["b","e","s","t"]]
# a=list[0]+list[1]+list[2]
# b=a
# print(b)
# s = ""
# s = s.join(b)
# print(s)




# # 7 max list
# list=[1,3,[1],[1,2],4,[1,2,3,4],4]
# i=0
# max=0
# while i<len(list):
#     if type(list[i])==list:
#         if list[i]<max:
#             max=list[i]
#             m=list[i]
#     i+=1
# print(max)




# # 8 saprate string values
# list=[11,12.9,3,11,"python","js"]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==str:
#         # print(list[i])
#         a.append(list[i])
#     i+=1
# print(a)



# # 9 max list and sum
# a=[[1,2,3],[3,5,9,99],[0,1,12],[2,3,3,4,5]]
# max=0
# i=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         m=a[i]
#     i+=1
# b=m
# j=0
# sum=0
# pro=1
# while j<len(b):
#     sum=sum+b[j]
#     pro=pro*b[j]
#     j+=1
# print("big list:-",b,max,"\nsum of max list :-",sum,"\nproduct of max list:-",pro)



# # 10 each element of list multiplay by 2
# list=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<len(list):
#     multiplaye=list[i]
#     print(multiplaye*2)
#     i+=1


# # 11 count of the number
# list1=[10,12,13,10,12,11,12,13,15,15]
# newlist=[]
# i=0
# while i<len(list1):
#     j=0
#     count=0
#     while j<len(list1):
#         if list1[i]==list1[j]:
#             count=count+1
#             h=list1[i]
#         j=j+1
#     i=i+1
# if count>2 or count<2:
#     if h not in newlist:
#         newlist.append(h)
# print(newlist)



# # 12 how many palindrome is present is a list
# a=["pradnya","sanju","mom","nitin","121","madam"]
# newlist=[]
# for i in a:
#     h=list(i)
#     j=len(h)-1
#     b=[]
#     while j>=0:
#         b.append(h[j])
#         j=j-1
#         j="".join(b)
#         newlist.append(j)
#         # print(newlist)
# count=0
# for k in range(len(a)):
#     if a[k]==newlist[k]:
#         count=count+1
# print(a[k])
# print(count)



# # 13 [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# a=[1,2,3,4,5,6]
# i=0
# k=[]
# while i<len(a)-1:
#     b=[a[i],a[i+1]]
#     k.append(b)
#     i=i+1
# print(k)


# # 14 each element of list adding 10
# a=[2,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     print(a[i]+10)
#     i+=1


# # 16 each element of list adding 3
# a=[3,8,9,5,0,5,0,3]
# i=0
# while i<len(a):
#     a[i]=a[i]+3
#     i+=1
# print(a)







# a=[2,3,4,5,[1,2,3,[5,6,7],8]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         b=0
#         while b<len(a[i]):
#             if type(a[i][b])==list:
#                 c=0
#                 while c<len(a[i][b]):
#                     sum=sum+(a[i][b][c])
#                     c+=1
#             else:
#                 sum=sum+(a[i][b])
#             b+=1
#     else:
#         sum=sum+(a[i])
#     i+=1
# print(sum)

