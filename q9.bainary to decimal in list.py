num=int(input("enter number:"))
sum=0
i=0
while num!=0:
    r=num%10
    sum=sum+r*pow(2,i)
    num=num//10
    i=i+1
print("decimal:",sum)