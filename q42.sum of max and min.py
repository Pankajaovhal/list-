a=[12,45,86,34,97,74,1,51,28]
i=0
max=0
min=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    i=i+1
print("max:",max)
print("min",min)
print("sum:",max+min)