#1.1, 1.2
def numAddition(firstNumber, secondNumber):
    return firstNumber + secondNumber

#2
def numIncrement(input):
    return input + 1

#3
def timeMinToSec(minutes):
   seconds = minutes * 60
   return seconds

#4 
def tri_area(base, height):
    area = base * height / 2
    return area

#5
def returnRemainder(numOne, numTwo):
    return numOne % numTwo

#7
def sumPolygonalAngle(sides):
    # (n-2) x 180
    return (sides - 2) * 180


#8 
import hashlib
def getSHA256(str):
    sha_sig = \
        hashlib.sha256(str.encode()).hexdigest()
    return sha_sig
#A simple test of hashing in python, it's nice and simple

#9a
def payrollCalculation(employee, minutes, rate = 7.60): #rate is £/Hour
    hours = minutes / 60
    pay = rate * hours 
    return employee + " is owed: £" + "{:.2f}".format(pay)
#Challenge of my own creation, allowed me to recall the formulas I once used somewhat, however simplified this may be

def payrollCalculationWithMin(employee, minutes, rate= 7.60, minPay = 50): #rate is £/Hour
    hours = minutes / 60
    additional = ""
    pay = rate * hours 

    if (pay <= minPay):
        pay = minPay
        additional = " (Did not reach minimum, and was subsidised)"
    
    return employee + " is owed: £" + "{:.2f}".format(pay) + additional
#Addition to my personal challenge, this would, in theory be set in an employee file in a finished system

def wageCalc(name, rate, *minutes):
    pay = 0
    for days in minutes:
        hours = days / 60
        pay += rate * hours
    return name + " is owed: £" + "{:.2f}".format(pay)
#Were this not a standalone function, it may well call on the individual day calculations and run through that 5 times, rather than accepting an undefined number of args


