##Import other files

import numberRelated as a
import wordRelated as b


##I began this looking primarily at Math related coding challenges

##1.1: Create a function that takes two numbers as arguments and return their sum.
print(a.numAddition(3, 2))
print("Previous result should be: 5")
print(a.numAddition(-3, -6))
print("Previous result should be: -9")
print(a.numAddition(7, 3))
print("Previous result should be: 10")
# Notes: Simple as can be, as expected

##1.2: Allow for the Addition function to take user input
firstNum = int(input("Enter your first number: "))
secondNum = int(input("Enter your second number: "))
print(a.numAddition(firstNum, secondNum))
##Notes: A slight hiccup here, which is that you need to convert the user input into an integer
##as variables are typeless by default so it takes the user input as a string, which wasn't accounted for

##2. Create a function that takes a number as an argument, increments the number by +1 and returns the result.
print(a.numIncrement(0))
print(a.numIncrement(9))
print(a.numIncrement(-3))
##Notes: Simple as you'd expect

##3 Write a function that takes an integer [minutes] and converts it to seconds.
print(a.timeMinToSec(5))
print(a.timeMinToSec(3))
print(a.timeMinToSec(2))
##Notes: This was only even slightly difficult because I was getting mixed up based on the very old knowledge
## from a payroll calculation for a manufacturing control system

##4. Write a function that takes the base and height of a triangle and return its area.
print(a.tri_area(3, 2))
print(a.tri_area(7, 4))
print(a.tri_area(10, 10))
##With the calculation provided two number operations are incredibly easy.

##5. Return the Remainder from Two Numbers
print(a.returnRemainder(1, 3))
print(a.returnRemainder(3, 4))
print(a.returnRemainder(5, 5))
print(a.returnRemainder(7, 2))
# Incredibly simple, it's just 'a % b'

# 7. Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
print(a.sumPolygonalAngle(3))
print(a.sumPolygonalAngle(4))
print(a.sumPolygonalAngle(6))
# Nice and simple when the formula is known, I need to start learning what some common formulas are, and keep a cheatsheet for myself

# 8. Encode string in SHA256
print(a.getSHA256("password123"))

# 9a. (Personal) Create a simple payroll calculation, that works take an employee name, minutes, and their rate in £/Hour
print(a.payrollCalculation("John Doe", 60, 7.60))
print(a.payrollCalculation("Sajid Alam", 450, 7.60))

# 9b. (Personal) Create a minimum payment for the previous function, that will trigger if an employee has not put in enough hours to reach it and replace it in that case
print(a.payrollCalculationWithMin("Johnny Dove", 510, 7.60))
print(a.payrollCalculationWithMin("Salam Ajid", 60, 7.60))

# 9c. (Personal) Create a function to run the previous function 5 times, to simulate a week, and calculate the final wage
print(a.wageCalc("Sajid", 7.60, 510, 450, 60, 260, 150))

##### Word Operations begin here
##6. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ...
## and space after each, and then the word is pronounced with a question mark ?.

print(b.wordStutter("incredible"))
print(b.wordStutter("enthusiastic"))
print(b.wordStutter("outstanding"))

##An example of my need to default to regular expressions, this was my first successful attempt at completing this challenge

print(b.simpleWordStutter("incredible"))
print(b.simpleWordStutter("enthusiastic"))
print(b.simpleWordStutter("outstanding"))
# This is a simpler version of the above, and does exactly the same with less lines.
# I need to learn to not overthink my code, and take the simplest route without cutting corners in ways that could compromise the software.
# this challenge did not in anyway need such a flexible solution as regex, but it was simpler in my head than three lines of code.
