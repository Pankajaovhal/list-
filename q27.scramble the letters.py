# Write a Python program to scramble the letters of string in a given list. 
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']



# a=['Python', 'list', 'exercises', 'practice', 'solution']
# i=0
# while i<1:
#     s=a[2:3]+a[5:]+a[0:1]+a[3:4]+a[1:2]+a[4:5]
#     print(s)
#     i=i+1



# num=int(input("enter the number"))
# i=1
# sum=0
# while i<num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1
# if sum==num:
#     print("prefect number")
# else:
#     print("not prefect num")


# from random import shuffle

# def shuffle_word(text_list):
#     text_list = list(text_list)
#     shuffle(text_list)
#     return ''.join(text_list)

# text_list = ['Python', 'list', 'exercises', 'practice', 'solution'] 
# print("Original list:")
# print(text_list)
# print("\nAfter scrambling the letters of the strings of the said list:")
# result =  [shuffle_word(word) for word in text_list]
# print(result) 