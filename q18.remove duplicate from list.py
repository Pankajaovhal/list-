# a=[10,20,30,20,10,50,60,40,80,50,40]	
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
# print(dup_items)


# a=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
# # # b=[]
# # # for i in a:
# # #     if i not in b:
# # #         b.append(i)
# # # print(b)

# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b) 


list1 = [1, 3, 5,4,3, 9]
list2=[1, 2, 4, 6,3, 8]
i=0
b=[]
list2.extend(list1)
while i<len(list2):
    if list2[i] not in b:
        b.append(list2[i])
    i+=1
print(b)



# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# i=0
# b=[]
# while i<len(list2):
#     if list2[i] not in list1:
#         b.append(list2[i])
#     # if list2[i] not in list1:
#     #     b.append(list2[i])
#     i+=1
# print(b)