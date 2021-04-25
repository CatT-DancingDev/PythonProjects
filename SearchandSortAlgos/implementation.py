###########################################################################################################
#
# Program:      Search and Sort
# Module:       implementation.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/19/2020
#
############################################################################################################
#
# Description:  This module defines the search and sort algorithms as described in Assignment #5, as well
#               as the user interface for each search or sort program.
#
########################################  FUNCTION LIST #####################################################
#
# Function 1:   radixSort10(array)
# Function 2:   radix10Interface()
# Function 3:   radixSort1(array)
# Function 4:   radix1Interface()
# Function 5:   mergeList(first, second)
# Function 6:   mergeSort(array)
# Function 7:   mergeSortInterface()
# Function 8:   binarySearch(array, low, high, target, k)
# Function 9:   binarySearchInterface()
# Function 10:  menu()
#
######################################### IMPORTS ###########################################################

import random
    # Used in mergeSortInterface()
    
##############################################################################################################
#
# Function 1:   radixSort10(array)
#
# Parameters:   int array - input array
# Return Type:  int array
#
# Purpose:      This function will return a sorted array of type int. The process includes use of 10
#               auxiliary lists to store processed values in. 
#
##############################################################################################################

def radixSort10(array):
    
    ### VARIABLES ###
    n = len(array)      # Length of input array 
    temp = [] * n       # Temporary Array
    exp = 1             # Current base10 exponent
    
    aux = [[] * n for z in range(10)]   # 10 auxiliary lists

    ### PROCESS - This will process up to 3 digits in each array element (1s, 10s, 100s)
    while exp <= 100:

        # For each number 0 - 9, for each item in input array:
        for a in range(10):      
            for i in array:
                # If the current place(1s, 10s, 100s) of current item matches the number a,
                # add it to the auxiliary list corresponding to that number.
                if (i // exp) % 10 == a:
                    aux[a].append(i)
        # Check all auxiliary lists.
        for a in range(10):
            # If not empty, append each item in the list to temp
            if aux[a]:
                for i in aux[a]:
                    temp.append(i)
        
        # Copy all elements of temp to array
        for i in range(n):
            array[i] = temp[i]
        # Clear auxiliary lists
        for list in aux:
            list.clear()
        # Clear temp list
        temp.clear()
        # Get next exponent of 10
        exp = exp * 10
        
    return array

##############################################################################################################
#
# Function 2:   radix10Interface()
#
# Parameters:   noArgs
# Return Type:  none
#
# Purpose:      This function will get obtain int array elements from user, and output the array as entered 
#               and the sorted array.  
#
##############################################################################################################

def radix10Interface():
    
    ### VARIABLES ###
    array1 = []         # input array
    done = False        # loop condition
    
    ### PROCESS - Obtain valid integers 0 - 999 from user. If valid integer is entered, add to list
    while not done:
        try: 
            number = int(input("Please enter a number 0 - 999. Enter -1 when finished.\n"))
            if number == -1:
                if len(array1) < 1:
                    print("Must have at least one element in list.\n")
                    continue
                done = True
                
            elif number >= 0 and number <= 999:
                array1.append(number)
                continue
            else:
                print("Invalid number. Please try again.\n")
        except ValueError:
            print("Invalid Entry. Please try again.\n")
            continue
    ### OUTPUT ###    
    print("\nArray as entered: ", array1)
    print("\nRadix10 sorted array: ", radixSort10(array1))

##############################################################################################################
#
# Function 3:   radixSort1(array)
#
# Parameters:   int array - input array
# Return Type:  int array
#
# Purpose:      This function will return a sorted array of type int. The process includes use of 1
#               temporary list to store processed values in. 
#
##############################################################################################################

def radixSort1(array):
    
    ### VARIABLES ###
    n = len(array)      # Length of input array 
    temp = [] * n       # Temporary Array
    exp = 1             # Current base10 exponent
    
    ### PROCESS - This will process up to 3 digits in each array element (1s, 10s, 100s)
    while exp <= 100:
        # For each number 0 - 9, for each item in input array:
        for a in range(10):
            for i in array:
                # If the current place(1s, 10s, 100s) of current item matches the number a,
                # add it directly to the temp list
                if (i // exp) % 10 == a:
                    temp.append(i)
                    
        # Copy all elements of temp to array            
        for i in range(n):
            array[i] = temp[i]
            
        # Clear temp list
        temp.clear()
        
        # Get next exponent of 10
        exp = exp * 10
    return array

##############################################################################################################
#
# Function 4:   radix1Interface()
#
# Parameters:   noArgs
# Return Type:  none
#
# Purpose:      This function will obtain int array elements from user, and output the array as entered 
#               and the sorted array.  
#
##############################################################################################################

def radix1Interface():
    ### VARIABLES ###
    array1 = []         # input array
    done = False        # loop condition

    ### PROCESS - Obtain valid integers 0 - 999 from user. 
    while not done:
        try: 
            number = int(input("Please enter a number 0 - 999. Enter -1 when finished.\n"))

            # Array size must be larger than 1 
            if number == -1:
                if len(array1) < 1:
                    print("Must have at least one element in list.\n")
                    continue
                done = True
                
            # If valid integer is entered, add to list    
            elif number >= 0 and number <= 999:
                array1.append(number)
                continue
            
            # If not, try again
            else:
                print("Invalid number. Please try again.\n")
                
        except ValueError:
            print("Invalid Entry. Please try again.\n")
            continue
        
    ### OUTPUT ###
    print("\nArray as entered: ", array1)
    print("\nRadix1 sorted array: ", radixSort1(array1))
    
##############################################################################################################
#
# Function 5:   mergeLists(first, second)
#
# Parameters:   first - sorted array, second - sorted array
# Return Type:  array - merged list
#
# Purpose:      This function will merge two lists together, returning a sorted list that contains all the
#               elements of first and last.
#               * This function is modified from textbook function mergeList(first, second, array)
#
##############################################################################################################

def mergeLists(first, second) :
    
    ### VARIABLES ###
    array = [0] * (len(first) + len(second))    # Initialize Array to be returned by function
    iFirst = 0                                  # Next element to consider in the first list
    iSecond = 0                                 # Next element to consider in the second list
    j = 0                                       # Next open index in array

    # While the counters are not at the ends of their respective lists,
    # move the smaller element into return array
    while iFirst < len(first) and iSecond < len(second):
        if first[iFirst] < second[iSecond]:
            array[j] = first[iFirst]
            iFirst = iFirst + 1
        else:
            array[j] = second[iSecond]
            iSecond = iSecond + 1
        j = j + 1
    # Copy any remaining entries of the first list
    while iFirst < len(first):
        array[j] = first[iFirst]
        iFirst = iFirst + 1
        j = j + 1
    # Copy any remaining entries of the second list
    while iSecond < len(second):
        array[j] = second[iSecond]
        iSecond = iSecond + 1
        j = j + 1
    
    return array

##############################################################################################################
#
# Function 6:   mergeSort(array)
#
# Parameters:   array - input array
# Return Type:  array
#
# Purpose:      This function uses the merge sort algorithm to separate input list into sublists of size 2,
#               then uses mergeList(first,last) to iteratively merge the lists into a single sorted list.
#               * This function does not use recursion, per the assignment instructions.
#
##############################################################################################################

def mergeSort(array):
    
    # if array length is 1 or 0, return array as-is.
    if len(array) <= 1:
        return array

    ### VARIABLES ###
    aux = [[] * int(len(array) / 2) for z in range(int(len(array)/2)) ]  # List of sub-lists 
    i = 0           # Iterates even indexes of input array
    j = 1           # Iterates odd index of input array
    a = 0           # Iterates each index of aux

    # PROCESS - Separate input array into sorted sublists of 2;
    #           store sublists in aux
    while i < (len(array) - 1) and j < (len(array)):

        # If equal, append to current sublist in any order
        if array[i] == array[j]:
            aux[a].append(array[i])
            aux[a].append(array[j])

        # Else, sort the two elements into a sublist of two
        else:
            aux[a].append(min(array[i], array[j]))
            aux[a].append(max(array[i], array[j]))
        # Increment array indexes by 2, increment aux index by 1
        i = i + 2
        j = j + 2
        a = a + 1
    
    # PROCESS - Merge all sublists, and remove empty lists
    while len(aux) > 1:
        a = 0
        # For every 2 lists in aux, merge and store in temp
        while a < (len(aux) - 1):
            temp = mergeLists(aux[a], aux[a + 1])
            aux[a].clear()

            # Copy temp list to current sublist
            for item in temp:
                aux[a].append(item)
            # Clear the next sublist (since it was merged with current)
            aux[a + 1].clear()
            # Increment current by 2, clear temp list for next iteration
            a = a + 2        
            temp.clear()
            
        # Remove empty lists from aux
        aux = list(filter(None, aux)) 
    # Array should be size 1
    array = aux[0]
    
    return array

##############################################################################################################
#
# Function 7:   mergeSortInterface()
#
# Parameters:   noArgs
# Return Type:  none
#
# Purpose:      This function will get obtain the array size from user. The function will use random.randint()
#               to assign values to the list. It will output the sorted array using mergeSort(array)
#
##############################################################################################################
def mergeSortInterface():
    valid = False       # loop condition

    ### PROCESS - Obtain size of array from user. Must be integer greater than 0
    while not valid:
        try:
            size = int(input("Please enter the size of your array. It must be a multiple of 2.\n"))
            if size % 2 != 0 or size < 1:
                print("Must be a multiple of 2 greater than 0. Please try again.\n")
                continue
            valid = True
        except ValueError:
            print("Invalid entry. Please try again.\n")
            continue
    # Initialize array    
    array1 = [] * size

    # Assign random values
    for i in range(size):
        number = random.randrange(1000)
        array1.append(number)

    ### OUPUT ###    
    print("\nRandom Array: ", array1)
    print("\nMerge sorted array: ", mergeSort(array1))

##############################################################################################################
#
# Function 8:   binarySearch(array, low, high, target, k)
#
# Parameters:   array - input array, low - low index, high - high index, target - search item,
#               k - stores mid index
#
# Return Type:  int
#
# Purpose:      This function uses binary search algorithm to determine if a target value is in a given list,
#               If item is in list, it returns the index of the item.
#               If item is not in list, it returns the index where the item should be inserted
#               * Modified from textbook function binarySearch(array, low, high, target)
#
##############################################################################################################

def binarySearch(array, low, high, target, k) :
    
    if low <= high:
        mid = (low + high) // 2     # Calculate mid
        k = mid                     # To formulate where target should be inserted

        # If target in array, find index of target recursively, include k in function parameters
        if array[mid] == target:
            return mid
        elif array[mid] < target :
            return binarySearch(array, mid + 1, high, target, k)
        else:
            return binarySearch(array, low, mid - 1, target, k - 1 )
    # Target not in array. return (-(insertion index))
    else:
        return - (k) - 1
##############################################################################################################
#
# Function 9:   binarySearchInterface()
#
# Parameters:   noArgs
# Return Type:  none
#
# Purpose:      This function will get obtain the array size from user. The function will obtain array elements
#               from user. It will obtain a target from the user. It will determine whether the array and
#               target are numeric or not. It will sort the list, and use binarySearch(a,l,h,t,k) to determine
#               whether or not the element is in the list, and output the result.
#
##############################################################################################################
def binarySearchInterface():
    valid = False           # loop condition

    ### PROCESS - get array size from user
    while not valid:
        try:
            size = int(input("Please enter the size of your array.\n"))
            if size < 1:
                print("Array needs to be at least one element long.")
                continue
            valid = True
        except ValueError:
            print("Invalid entry. Please try again.\n")

            continue
    # Initialize array
    array1 = [] * size

    # Fill Array
    for i in range(size):
        item = input("Please enter an item to add to the list.\n")
        if item.isnumeric():
            item = int(item)
        array1.append(item)
    # Sort Array    
    array1.sort()

    # Get target item from user
    target = input("Please enter a value to search for. \n")
    if target.isnumeric():
        target = int(target)
    # Binary Search    
    index = binarySearch(array1, 0, size - 1, target, 0)

    ### OUTPUT ###
    print("Your sorted list: ", array1)
    if index >= 0:
        print("\nYour item is in the list at index ", index)
    else:
        print("\nYour item is not in the list. It should be inserted at index ", (-1 * index))
        
##############################################################################################################
#
# Function 10:   menu()
#
# Parameters:   noArgs
# Return Type:  none
#
# Purpose:      This function will continuously ask user to select which program they want to run, and run the
#               appropriate program
#
##############################################################################################################

def menu():
    done = False            # loop condition
    
    print("************* Welcome to the Search and Sort Program **************\n\n")

    ### PROCESS ###
    while not done:
        
        # Print menu selections
        print("SELECTION MENU")
        print("(1) - Radix Sort with 10 Auxiliary Lists")
        print("(2) - Radix Sort with 1 Auxiliary List")
        print("(3) - Merge Sort")
        print("(4) - Binary Search\n\n\n")

        # Get valid selection, run corresponding function
        valid = False
        while not valid:
            choice = input("Please enter the number for you selection. Type and enter DONE to quit.\n")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "DONE":
                valid = True
            else:
                print("Invalid entry. Please try again.")
                continue
            if choice == "DONE":
                print("Thank you for using Search and Sort Program. Have a great day!")
                done = True
                return
            elif choice == "1":
                print("\n ***Radix 10 Sort Program***\n")
                radix10Interface()
                print("\n\n********************************\n\n")
            elif choice == "2":
                print("\n ***Radix 1 Sort Program***\n")
                radix1Interface()
                print("\n\n********************************\n\n")
            elif choice == "3":
                print("\n ***Merge Sort Program***\n")
                mergeSortInterface()
                print("\n\n********************************\n\n")
                
            elif choice == "4":
                print("\n ***Binary Search Program***\n")
                binarySearchInterface()
                print("\n\n********************************\n\n")
                
######################################## END IMPLEMENTATION.PY #####################################################
           

        
    
    






     

