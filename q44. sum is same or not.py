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


from random import shuffle

def shuffle_word(text_list):
    text_list = list(text_list)
    shuffle(text_list)
    return ''.join(text_list)

text_list = ['Python', 'list', 'exercises', 'practice', 'solution'] 
print("Original list:")
print(text_list)
print("\nAfter scrambling the letters of the strings of the said list:")
result =  [shuffle_word(word) for word in text_list]
print(result) 