n=int(input())
if n >100 or n<0:
    print("invalid")
elif n>=90:
    print("Grade->A")
elif n>=75:
    print("Grade->B")
elif n>=50:
    print("Grade->C")
else:
    print("Fail")
