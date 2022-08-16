# import random
# lower_case="abcdefghijklmnopqrstuvwxyz"
# upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# num="0123456789"
# symbol="@#*.-_"
# ans=lower_case+upper_case+num+symbol
# lenght= int(input("enter lenght of password:"))
# password="".join(random.sample(ans,lenght))
# print("generated password is:",password)


# import string
# import random 

# length=int(input("enter the length : "))
# a=[]
# letter=string.ascii_letters
# digits=string.digits
# special=string.punctuation
# a.append((special+letter+digits))
# b=str(a)
# f=random.sample(b,length)
# password="".join(f)

# print(password)



import string
import random
length=int(input("enter the lenght:"))
a=[]
letter=string.ascii_lowercase
letter1=string.ascii_uppercase
digit=string.digits
special=("~``!@#$%^&*()_-+=<,./|'")
b=letter+letter1+digit
a.append(b)
f=random.sample(b,length)
password="".join(f)
password.replace(" ","")

print(password)
