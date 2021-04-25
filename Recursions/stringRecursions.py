######################################################################################################
#
# Program:      Fun With Recursion
# Module:       stringRecursions.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/14/2020
#
######################################################################################################
#
# Description:  This module defines recursive functions as described in
#               Assignment #4, string recursions. 
#
############################# MAIN PROGRAM FUNCTION LIST #############################################
#
# Function 1:   stringLength(string)
# Function 2:   countSubstring(n)
# Function 3:   userInterface()
#
#######################################################################################################
#
# Function 1:   stringLength(string)
#
# Parameters:   string = string to be processed
# Return Type:  int
#
# Purpose:      This function will use recursion to calculate the length of a string
#
#######################################################################################################

def stringLength(string):
    # base case
    if string == "":
        return 0
    
    # Function recursion 
    else:
        return 1 + stringLength(string[1:])

#######################################################################################################
#
# Function 2:   countSubstring(string, a, b, length)
#
# Parameters:   string = string to be processed, a = string index,
#               b = string index, length = counter 
# Return Type:  int
#
# Purpose:      This function will use recursion to calculate the number of substrings with matching
#               first and last characters
#
#######################################################################################################

def countSubstring(string, a, b, length):
    # Base case 1
    if length == 0:
        return 0

    # Base case 2
    elif length == 1:
        return 1
    # Process involving recursive calls and comparing indexes
    else:
        count = (countSubstring(string, a + 1, b, length - 1) + countSubstring(string, a, b - 1, length - 1) - countSubstring(string, a + 1, b - 1, length - 2))
        if string[a] == string[b]:
            count += 1
        return count

#######################################################################################################
#
# Function 3:   userInterface()
#
# Parameters:   noArgs

# Return Type:  None
#
# Purpose:      This function prompts user for a string, and uses them to call the functions in this
#               module. Note - the recurive process for countSubstring can be quite lengthy. Keep this 
#
#######################################################################################################

def userInterface():
    # String to be analyzed
    string = input("Please enter a string to analyze. For best results keep the string fairly short, as this recursion method can be exponentially time-consuming.\n")

    # Output - Both Functions
    print("String length including spaces and punctuation: " , stringLength(string))
    print("Please wait. This next recursion can be SLOW.")
    print("Number of substrings with same first and last character: " , countSubstring(string, 0, len(string) - 1, len(string)))


          
                
    
    
