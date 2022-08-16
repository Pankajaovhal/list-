marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
i=0
length=len(marks)
l=0
m=0
while i<length:
    marks=marks[i]
    if marks<50:
        l=l+1
    else:
        m+=1
    i+=1
print("marks less than 50:",l)
print("marks more than 50:",m)


