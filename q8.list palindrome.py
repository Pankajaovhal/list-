# a=['n','i','t','i','n']
# i=0
# b=[ ]
# while i<len(a):
#     b.append(a)
#     i=i+1
#     print(b)
# if b==a or a==b:
#     print("it's palindrome.")
# else:
#     ("it's not palindrome.")




# # a=['n','i','t','i','n']
# a=input("enter:")
# i=0
# l=int(len(a))
# while i<int(l/2+1):
#     if a[i]==a[-i-1]:
#         i+=1
#     else:
#         break
# if i<(l/2):
#     print("not")
# else:
#     print("yes")


a=input("enter:")
b=a[-1::-1]
if a==b:
    print("palindrome")
else:
    print("not palindrome")