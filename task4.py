
import math

def sum_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Calculate Triangle Area")
        print("6. Calculate Circle Area")
        print("7. Calculate Rectangle Area")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Sum:", sum_numbers(num1, num2))
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Difference:", subtract_numbers(num1, num2))
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Product:", multiply_numbers(num1, num2))
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Quotient:", divide_numbers(num1, num2))
        elif choice == "5":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Triangle Area:", calculate_triangle_area(base, height))
        elif choice == "6":
            radius = float(input("Enter the radius of the circle: "))
            print("Circle Area:", calculate_circle_area(radius))
        elif choice == "7":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Rectangle Area:", calculate_rectangle_area(length, width))
        elif choice == "8":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()
