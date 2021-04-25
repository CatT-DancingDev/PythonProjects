######################################################################################################
#
# Program:      Fun With Recursion
# Module:       main.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/14/2020
#
######################################################################################################
#
# Description:  This main test program will test the recursive functions from the following modules:
#               - stringRecursions.py
#               - listRecursions.py
#               - mathematicalRecursions.py
#
############################# MAIN PROGRAM FUNCTION LIST #############################################
#
# Function 1:     main()
#
############################# MODULES AND LIBRARIES ##################################################

import listRecursions 
import stringRecursions 
import mathematicalRecursions
import os
######################################################################################################
#
# Function 1:   main()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will run all test functions 
#
#######################################################################################################

def main():
    # Test 1
    print("*****STRING RECURSIONS*****\n")
    stringRecursions.userInterface()

    # Test 2
    print("\n*****LIST RECURSIONS*****\n")
    listRecursions.userInterface()

    # Test 3
    print("\n*****MATH RECURSIONS*****\n")
    mathematicalRecursions.userInterface()

    # pause
    os.system("pause")
    
########################################################################################################
main()
    
    
