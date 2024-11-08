import math

"""
The Geometeric Shapes Calculator program addresses the real-world need for quick and accurate calculations of 
areas, perimeter, volumes and surface areas of common geometric shapes, which is crucial in fields such as 
construction, engineering, product design and education. The program enhances efficiency, accuracy and productivity
in various professional and educational settings.

A user has the opportunity to choose from four diiferent shapes and the the user can enter a required argument
and the program will calculate the area, volume or surface area of the shape.

Example:
If a user makes a choice 1 which is circle, the program asks for the radius of the circl and computes the 
area and circumference of the circle.
If a user enters the radius of a circle as 7 the program computes the area and circumference of the cirlce 
as 60.82 and 27.65 respectively.
"""

# calculates the area of a circle and return the value
def circle_area(radius):
    area_of_circle = math.pi * (radius ** 2)
    return area_of_circle

# computes the circumference of a circle and return its value
def circle_circumference(radius):
    circumference_of_circle = 2 * math.pi * radius
    return circumference_of_circle

#computes the area of a rectangle and return its value
def rectangle_area(length, width):
    area_of_rectangle = length * width
    return area_of_rectangle

#computes the perimeter of rectangle and return its value 
def rectangle_perimter(length, width):
    perimeter_of_rectangle = 2 * (length + width)
    return perimeter_of_rectangle

#computes the volume of sphere and return its value
def sphere_volume(radius):
    volume_of_sphere = 4 / 3 * math.pi * (radius ** 3)
    return volume_of_sphere

#computes the surface area of a sphere and returns its value
def sphere_surface_area(radius):
    surface_area_of_sphere = 4 * math.pi * (radius ** 2)
    return surface_area_of_sphere

#computes the volume of cone and returns its value
def cone_volume(radius, height):
    #the parameter height is the vertical height of the cone
    volume_of_cone = 1 /3 * math.pi * (radius ** 2) * height
    return volume_of_cone

# computes total surface area of a solid cone and returns its value
def surface_area_of_cone(radius, length):
    # the parameter length is the slant height of the cone
    cone_total_surface_area = math.pi * radius * (radius + length)
    return cone_total_surface_area

def main():
    try:
        #this block of code allows the user to choose a shape that the user wants to compute
        print("Geometeric Shapes Calculator")
        print("Please choose a shape...")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Sphere")
        print("4. Cone")
        print("5. Exit")

        #this code ask the user to choose from the shapes listed above
        choice = int(input("Choose a Geometric Shape: "))

        # this block of code runs if the user chooses option 1 which computes the area
        # and circumference of the circle
        if choice == 1:
            radius = float(input("Enter the radius of the circle: "))
            print(f"Area: {circle_area(radius):.2f}")
            print(f"Circumference: {circle_circumference(radius):.2f}")

         # this block of code runs if the user chooses option 2 which computes the area
        # and perimeter of the rectangle
        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"Area: {rectangle_area(length, width):.2f}") # round the value to two decimal places
            print(f"Perimeter: {rectangle_perimter(length, width):.2f}")  # round the value to two decimal places

        # this block of code runs if the user chooses option 3 which computes the volume
        # and surface of the sphere
        elif choice == 3:
            radius = float(input("Enter the radius of the sphere: "))
            print(f"Volume: {sphere_volume(radius):.2f}") # round the value to two decimal places
            print(f"Surface Area: {sphere_surface_area(radius):.2f}") # round the value to two decimal places


         # this block of code runs if the user chooses option 4 which computes the volume
         # and urface area of the cone
        elif choice == 4:
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone(vertical height of the cone): "))
            print(f"Volume: {cone_volume(radius, height):.2f}") # round the value to two decimal places

            print("Let's help you compute the surface area of your cone")
            length = float(input("Enter the length of the slant height of the cone: "))
            print(f"Surface Area: {surface_area_of_cone(radius, length):.2f}")  # round the value to two decimal places

        # the program exits if the user choses option 5
        elif choice == 5:
            print("Exiting Geometric Shapes Calculator.....")
            
        else:
            print("Invalid choice. Please Choose a valid option")

        
    # This is the code the computer executes if the code in the try block cause a function to raise a 
    # ZeroDivisionError
    except ZeroDivisionError as zero_div_eer:
        print(zero_div_eer)

    # This is the code the computer excutes if the code in the try block cause a function to raise a
    # TypeError
    except TypeError as type_eer:
        print(type_eer)
    
    # This is the code the computer executes if the code in the try block cause a function to raise a
    # ValueError
    except ValueError as value_eer:
        print(f"{value_eer}")

# Call main to start this program.
if __name__ == "__main__":
    main()