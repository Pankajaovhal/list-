# Write a Python program to sum two or more lists, the lengths of the lists may be different. 
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]

a=[[1,2,4],[2,4,4],[1,2]]
i=0
sum=0
s=[]
while i<len(a):
    k=0
    while k<len(a[i]):
        j=0
        while j<len(a[i]):
            sum=a[i][j]+sum

            j=j+3
        s.append(sum)
        k=k+1
    i=i+1
print(s)
        
