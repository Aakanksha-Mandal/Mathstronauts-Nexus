shape = input("Please enter the shape you want to calculate the area of: ")

if (shape.lower() == "rectangle"):
    width = float(input("Please enter the width of the rectangle: "))
    length = float(input("Please enter the length of the rectangle: "))

    area = width*length
    print("The area of your rectangle is", area)

elif (shape.lower() == "circle"):
    import math
    radius = float(input("Please enter the radius of the circle: "))

    area = math.pi*radius*radius
    print("The area of your circle is", area)

elif (shape.lower() == "triangle"):
    base = float(input("Please enter the base of the triangle: "))
    height = float(input("Please enter the height of the triangle: "))

    area = base*height/2
    print ("The area of your triangle is", area)

else:
    print("Sorry shape not recognized.")
