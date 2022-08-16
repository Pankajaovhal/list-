zs=["Aries","Taurus","Gemini","Cancer","leo","Virgo","Libra","Scorpio","sagittarius","capricorn","Aquarius","Pices"]
i=0
while i<1:
    print("this program to know your horoscope.")
    date=int(input("enter your birth date:"))
    if date >31 or date<0:
        print("please enter the correct date.the date should not exceed 31\n")
        continue

    month=int(input("enter your birthday month in number format(for example 1 for january,2):"))

    if month >12 or month<0:
        print("please enter the correct month. the month should not exceed 12\n")
        continue
    if date >28 and month == 2:
        print("please enter the correct date." )


    if month==4:
        if date >20 and date >19:
            c=zs[0]
        # else:
        #     c=zs[1]
        print("your zs is",c)
    # elif month ==5:
    #     if date >20 and date >19:
    #         c=zs[1]
    #     # else:
        #     c=zs[3]
        # print("your zs is",c)
    i+=1



zs=["Aries","Taurus","Gemini","Cancer","leo","Virgo","Libra","Scorpio","sagittarius","capricorn","Aquarius","Pices"]
date=int(input("enter the num:-"))
month=input("enter the num:-") 
a=[]   
if month=="march" and date>21 or month=="april" and date<19:
                a.append((zs[0],"you have to"))
elif month=="april" and date>20 or month=="may" and date<20:
                a.append(zs[1],"")
elif month=="may" and date>21 or month=="jun" and date<20:
                a.append(zs[2],"")
elif month=="jun" and date>21 or month=="july" and date<22:
                a.append(zs[3],"")
elif month=="july" and date>23 or month=="aug" and date<22:
                a.append(zs[4],"")
elif month=="aug" and date>23 or month=="sep" and date<22:
                a.append(zs[5],"")
elif month=="sep" and date>23 or month=="oct" and date<22:
                a.append(zs[6],"")
elif month=="oct" and date>23 or month=="nov" and date<21:
                a.append(zs[7],"")
elif month=="nov"and date>22 or month=="dec" and date<21:
                a.append(zs[8],"")
elif month=="dec" and date>22 or month=="jan" and date<19:
                a.append(zs[9],"")
elif month=="jan" and date>20 or month=="feb" and date<18:
                a.append(zs[10],"")
elif month=="feb" and date>19 or month=="march" and date<20:
                a.append(zs[11],"")
else:
                print("your information is wrong")
print(a)              

