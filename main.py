# Assignment 1 - ANA1001
# Fatooma Iqbal - A00268573
###############################

#Question1
#I intend to create a simple greeting, basic calculator, basic loop, list manipulation

#Simple Greeting!
print("Hello, how are you doing today?")

#Simple Calculator
num1 = 5
num2 = 3

#Addition
print(num1 + num2)

#Subtraction
print(num1 - num2)

#Multiplication
print(num1 * num2)

#Division
print(num1 / num2)

#Basic Loop
for i in range(8):
  print("I am programming in python after " + str(i) + " years!")

#List Manipulation

fruits = ["apple", "banana", "orange", "guava", "kiwi"]
print("Original list:", fruits)
fruits.append("grape")
#append(takes only 1 argument at a time)
print("Updated list:", fruits)
fruits.append("cherry")
print("Updated list:", fruits)

#Question 2 'Storage & display of city names'
city = "Sudbury"
print(city.title())

#title() makes the first letter as upper case

city = "sialkot"
print(city.title())
#upper() makes all the letters as upper case
city = "san francisco"
print(city.title().upper())

#Question 3 'Storing & printing name in different cases'

first_name = "fatooma"
last_name = "iqbal"

# Uppercase
print(f"My name is {first_name.upper()} {last_name.upper()}.")

# Lowercase
print(f"My name is {first_name.lower()} {last_name.lower()}.")

# Title case
print(f"My name is {first_name.title()} {last_name.title()}.")

#Question 4 'Operations to equal 2023'
#Addition
addition_result = 2000 + 23
#Subtraction
subtraction_result = 2040 - 17
#Multiplication
multiplication_result = 101.15 * 20
#Division
division_result = 4046.2 / 2

# Printing messages using f strings
print(f"Adding 2000 and 23 equals {addition_result}")
print(f"Subtracting 17 from 2040 equals {subtraction_result}")
# Printing messages using join
print("Multiplying 101.15 by 20 equals " + str(multiplication_result) + ".")
print("Dividing 4046.2 by 2 equals " + str(division_result) + ".")
