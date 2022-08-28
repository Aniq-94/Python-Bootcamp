# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:11:24 2022

@author: aniqa
"""
#import library for logarithm
import math
#Welcome statement explaining the program to the user
  
print("TVM Calculator\nPlease enter all values in numerical format\nLeave whichever value you want to calculate blank.\nOnly one value can be calculated at a time.\nOnce you enter any value even as a string against a variable it can no longer be set as the variable being calculated and the program has to be restarted")


#set sol_variable to zero. This will help us to switch our equation based on whichever unknow we are trying to calculate
#sol_variable will be set based on which input the user leaves blank
#sol_variable == 1 => PV - The present value of the cash flows
#sol_variable == 2 => FV - The future value of the cash flows
#sol_variable == 3 => I - Interest rate (annualized)
#sol_variable == 4 => N - Number of compounding periods per year
#sol_varaible == 5 => T - Number of years

sol_variable=0

#Ask for inputs, inputs have to be taken in a specific sequence to ensure only one empty variable
#is entered, and to sequentially determine the value of the function argument

#Taking input for present value
pv=input("Enter Present Value:")
if pv=="":
    print("Solving for PV") #inform the user that the program will now solve for PV
    sol_variable=1          #sol_variable is set to 1 so that TVM solves for PV
else:
    while True:             #try except within while loop to ensure numerical value is entered
        try:                #loop is limited because once a string is entered user can no longer enter an empty value
            pv=float(pv)
            break
        except ValueError:
            pv=input("Invalid Input. Please enter numerical value for PV") 

#Taking input for Future Value
fv=input("Enter Future Value")
if sol_variable!=0 and fv=="": #checking if unknown has been set. Since equation cannot have two unknowns we need to restrict the user here
    fv=input("Unknown has already been set, please enter a numerical value for FV")
elif fv=="":
    print("Solving for FV") #inform the user that the program will solve for FV
    sol_variable=2          #sol_variable is set to 2 so that TVM solves for FV
else:
    while True:
        try:
            fv=float(fv)
            break
        except ValueError:
            fv=input("Invalid Input. Please enter numerical value for FV")

i=input("Enter interest rate")
if sol_variable!=0 and i=="": #checking if unknown has been set
    i=input("Unknown has already been set, please enter a numerical value for I")
    i=i/100
elif i=="":
    print("Solving for I")  #inform the user that program will solve for I
    sol_variable=3          #set sol_variable to 3 so that TVM calculates for I
else:
    while True:
        try:
            i=float(i)/100
            break
        except ValueError:
            fv=input("Invalid Input. Please enter numerical value for I")

n=input("Enter number of compounding periods per year")
if sol_variable!=0 and n=="":
    n=input("Unknown has already been set, please enter a numerical value for N")
elif n=="":
    print("Solving for N")  #inform user that program will solve for N
    sol_variable=4          #set sol_variable to 4 so that TVM calculates for N
else:
    while True:
        try:
            n=float(n)
            break
        except ValueError:
            n=input("Invalid Input. Please enter numerical value for N")
            
t=input("Enter number of years")
if sol_variable!=0 and t=="":
    t=input("Unknown has already been set, please enter a numerical value for T")
elif t=="":
    print("Solving for T")  #inform user that program will solve for T
    sol_variable=5          #set sol_variable to 5 so that TVM calculates for T
else:
    while True:
        try:
            t=float(t)
            break
        except ValueError:
            t=input("Invalid Input. Please enter numerical value for T")


if sol_variable==0:         #in case user enters a value for every variable
    print("No unknown entered. Program ending.")
#Actual calculation of unknown for each value of sol_variable. Based on TVM Formula: FV=PV*(1+I/N)^NT
else:
    if sol_variable==1:
        pv=fv/((1+i/n)**(n*t))
    elif sol_variable==2:
        fv=pv*((1+i/n)**(n*t))
    elif sol_variable==3:
        i=(((fv/pv)**(1/(n*t)))-1)*n
    elif sol_variable==4:
        n=i/(((fv/pv)**(1/(n*t)))-1)
    elif sol_variable==5:
        z=math.log(fv/pv)
        y=math.log(1+i/n)
        t=z/y/n
#print out solutions for user
print("I:",i*100)
print("PV:",pv)
print("FV:",fv)
print("N:",n)
print("T:",t)
