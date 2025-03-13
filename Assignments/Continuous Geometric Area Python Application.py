import time

print("Welcome to my Geometric Area Application!")
shape = input("Please enter the shape you want to calculate the area of or quit: ")

while (shape.lower != "quit"):

    if (shape.lower() == "rectangle"):
        width = float(input("Please enter the width of the rectangle: "))
        length = float(input("Please enter the length of the rectangle: "))

        area = width*length
        print("The area of your rectangle is", area)
        time.sleep(1)
        shape = input("\nPlease enter the shape you want to calculate the area of or quit: ")

    if (shape.lower() == "circle"):
        import math
        radius = float(input("Please enter the radius of the circle: "))

        area = math.pi*radius*radius
        print("The area of your circle is", area)
        time.sleep(1)
        shape = input("\nPlease enter the shape you want to calculate the area of or quit: ")

    if (shape.lower() == "triangle"):
        base = float(input("Please enter the base of the triangle: "))
        height = float(input("Please enter the height of the triangle: "))

        area = base*height/2
        print ("The area of your triangle is", area)
        time.sleep(1)
        shape = input("\nPlease enter the shape you want to calculate the area of or quit: ")

    if(shape.lower() == "quit"):
        print("Goodbye.")
        break
    else:
        print("Sorry shape not recognized.")
        shape = input("Please enter the shape you want to calculate the area of or quit: ")
    
    

    

