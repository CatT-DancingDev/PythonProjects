######################################################################################################
#
# Program:      Fun With Recursion
# Module:       mathematicalRecursions.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/14/2020
#
######################################################################################################
#
# Description:  This module defines recursive functions and helper functions as described in
#               Assignment #4, mathematical recursions. Functions 1 - 5 pertain to printing a diamond.
#               Function 6 is the multiplication function.
#
############################# MAIN PROGRAM FUNCTION LIST #############################################
#
# Function 1:   printSpaces(n)
# Function 2:   printStars(n)
# Function 3:   top(n, i)
# Function 4:   bottom(n, i)
# Function 5:   printDiamond(n)
# Function 6:   mult(a, b)
# Function 7:   userInterface()
#
#######################################################################################################
#
# Function 1:   printSpaces(n)
#
# Parameters:   n = number of spaces to be printed
# Return Type:  None
#
# Purpose:      This function will print n number of spaces 
#
#######################################################################################################

def printSpaces(n): 
      
    # base case 
    if (n == 0): 
        return; 
    print(" ", end = "") 
  
    # Function Recursion 
    printSpaces(n - 1) 
  
#######################################################################################################
#
# Function 2:   printStars(n)
#
# Parameters:   n = number of stars to be printed
# Return Type:  None
#
# Purpose:      This function will print n number of stars 
#
#######################################################################################################

def printStars(n): 
      
    # base case 
    if(n == 0): 
        return; 
    print("* ", end = "") 
  
    # Function Recursion
    printStars(n - 1) 
  
#######################################################################################################
#
# Function 3:   top(n, i)
#
# Parameters:   n = used to calculate number of iterations/how many spaces and stars to print,
#               i = constant - size of diamond
#
# Return Type:  None
#
# Purpose:      This function will print the top half of the diamond 
#
#######################################################################################################

def top(n, i): 
      
    # base case 
    if (n == 0): 
        return
    # process
    printSpaces(n - 1); 
    printStars(i - n + 1) 
    print("") 
  
    # Function Recursion 
    top(n - 1, i);
    
#######################################################################################################
#
# Function 4:   bottom(n, i)
#
# Parameters:   n = used to calculate number of iterations/how many spaces and stars to print,
#               i = constant - size of diamond
#
# Return Type:  None
#
# Purpose:      This function will print the bottom of the diamond 
#
#######################################################################################################

def bottom(n, i):
    # base case
    if i == 0:
        return
    # process
    printSpaces(n - i + 1)
    printStars(i - 1)
    print("")
    # Function Recursion
    bottom(n, i -1)
#######################################################################################################
#
# Function 5:   diamond(n)
#
# Parameters:   n = largest number of stars in one row of the diamond i.e diamond width

# Return Type:  None
#
# Purpose:      This function calls the top and bottom recursive functions to print a diamond of n width 
#
#######################################################################################################

def printDiamond(n):
    top(n,n)
    bottom(n,n)

#######################################################################################################
#
# Function 6:   mult(a, b)
#
# Parameters:   a = multiplicand, b = multiplier

# Return Type:  int
#
# Purpose:      This function uses recursion to find the product of a and b
#
#######################################################################################################

def mult(x, y):
    if x < y:
        return mult(y, x)
    elif y != 0:
        return x + mult(x, y - 1)
    else:
        return 0
    
#######################################################################################################
#
# Function 7:   userInterface()
#
# Parameters:   noArgs

# Return Type:  None
#
# Purpose:      This function collects 3 numbers from user, and uses them to call the functions in this
#               module.
#
#######################################################################################################

def userInterface():
    valid = False       ## Correct Input

    # Get multiplier and multiplicand
    while not valid:
        try:
            num1 = int(input("Please enter a positive integer. \n"))
            num2 = int(input("Please enter positive integer. \n"))
            if num1 < 0 or num2 < 0:
                print("Must be positive numbers.")
                continue
            valid = True
        except ValueError:
            print("Non-numeric value entered. Resetting questions.")
            continue

    # Output mult function   
    print("{} x {} = ".format(num1, num2) , mult(num1, num2))

    # Get size of diamond
    valid = False
    while not valid:
        try:
            size = int(input("\nPlease enter a number 1 - 35.\n"))
            if size < 1 or size > 35:
                continue
            valid = True
        except ValueError:
            print("Non-numeric value entered.")
            continue

    # Output diamond    
    printDiamond(size)

    

    
    
