side1= float(input("enter side 1"))
side2= float(input("enter side 2"))
side3= float(input("enter side 3"))
if side1 == side2 == side3:
    print("equilateral triangle")
elif side1 == side2 or side3 == side2 or  side3 ==side1:
    print("Isosceles triangle")
else:
    print("scalene triangle")


