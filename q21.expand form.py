# a=input
# b=len(str(a))
# i=b-1
# while i>=0:
#     c=a//(10**i)
#     d=c*(10**i)
#     a=a%(10**i)
#     print(d,"+",end="")
#     i-=1



list=[]
def l(a,b):
    for i in range(a,b):
        if i%2==0:
            c=list.append(i)
    return c
v=l(4,30)
print(v)
