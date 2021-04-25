######################################################################################################
#
# Program:      Fun With Recursion
# Module:       listRecursions.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/14/2020
#
######################################################################################################
#
# Description:  This module defines recursive functions as described in
#               Assignment #4, list recursions. 
#
############################# MAIN PROGRAM FUNCTION LIST #############################################
#
# Function 1:   possibleCombinations(arr,r)
# Function 2:   maximum(arr, low, high)
# Function 3:   userInterface()
#
#######################################################################################################
#
# Function 1:   possibleCombinations(arr,r)
#
# Parameters:   arr = array to be processed, r = length of combinations
# Return Type:  int [[]]
#
# Purpose:      This function will use recursion within a nested for loop to return a list of all
#               possible combinations of length r
#
#######################################################################################################

def possibleCombinations(arr, r):
    # base case
    if r==0:
        return [[]]
    
    # each new list
    combo=[]

    # Process - For each element in array, find all possible combos of r length
    n = len(arr)
    for i in range(n):
        # For each recursive call, take out the "1st" element, decrement r, 
        for c in possibleCombinations(arr[i+1:], r-1):
            combo.append([arr[i]]+c)
    return combo

#######################################################################################################
#
# Function 2:   maximum(arr, low, high)
#
# Parameters:   arr = array to be processed, low = low index, high = high index 
# Return Type:  int
#
# Purpose:      This function will use recursion to find the largest element in an array
#
#######################################################################################################

def maximum(arr, low, high):
    largest = 0   ## beginning largest value
    # base case 1
    if (low == high):
        return arr[low]
    else:
        # increment take out the "1st" element with each recursive call
        largest = maximum(arr, low +1, high)
        # base case 2
        if arr[low] >= largest:
            return arr[low]
        # Recursive call
        else:
            return largest
        


#######################################################################################################
#
# Function 3:   userInterface()
#
# Parameters:   noArgs

# Return Type:  None
#
# Purpose:      This function repeatedly prompts user for numbers to fill an array, then performs the
#               functions listed in this module on said array
#
#######################################################################################################

def userInterface():
    array = []      ## input array
    r = 0           ## combo length
    num = 0         ## numbers for array
    valid = False   ## input correct 
    
    # Fill array
    while num != -999 or not valid:
        try:
            num = int(input("Please enter a number to add to the array. Enter -999 when you are finished. \n"))
            if num == -999:
                
                # Array size must be greater than 0
                if not array:
                    print("Array must have at least one element.")
                    continue
                valid = True
                break
            array.append(num)

            
            
        except ValueError:
            print("Please enter a numeric value.")
            continue
        
    
    # print array
    print("Array: ")
    print(*array, sep = ", ") 
  
    # Get size of combinations - must be smaller than array length.
    valid = False
    while not valid:
        r = int(input("What size combinations do you wish to make?\n"))       
        if r <= len(array):
            valid = True
        else:
            print("Number must be equal to or smaller than the size of the array.")
            
    # Output Function 1
    print("Possible Combinations: of size {}: \n".format(r))
    print(possibleCombinations(array, r))

    # Output Function 2
    print("\nMaximum value in array: ", maximum(array, 0, len(array) -1))



