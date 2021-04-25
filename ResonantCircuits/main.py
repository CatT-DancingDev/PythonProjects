###############################################################################################
#
# Program:      Resonant Circuit Design
# Module:       main.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/07/2020
#
###############################################################################################
#
# Description:  This main test program will test the super class, ResonantCircuit, and the 
#               subclasses ParallelResonantCircuit, and SeriesResonantCircuit. For each test, 
#               the program  will ask the user to input values that describe a resonant frequency 
#               response: Resonant Frequency, Bandwidth, and Gain At Resonant Frequency. These 
#               functions will test the get, set, display, and constructor methods of the super
#               class and subclasses listed above.
#
############################# MAIN PROGRAM FUNCTION LIST ######################################
#
# Function 1:   testCase1()
# Function 2:   testCase2()
# Function 3:   testCase3()
# Function 4:   main()
#
############################# MODULES AND LIBRARIES ###########################################

from resonantCircuit import ResonantCircuit
from parallelResonantCircuit import ParallelResonantCircuit
from seriesResonantCircuit import SeriesResonantCircuit
import os

############################# FUNCTION DEFINITIONS ############################################
#
# Function 1:   testCase1()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will create one object from each of the classes, collect data from
#               user, use the data to set the values for the instance variables, design the 
#               necessary circuits, then display the description of the resonant frequency response
#               for each object, and the circuit design values. This function will allow multiple
#               successsive entries.
#
################################################################################################

def testCase1():
    
    print("Test Case 1 - One set of inputs to test all classes")

    #### VARIABLES ####
    enterData = "y"         # String - outer while loop control
    done = False            # Bool   - input while loop control
    rf = 0                  # Float  - Resonant Frequency     
    b = 0                   # Float  - Bandwidth
    k = 0                   # Float  - Gain at RF 
    
    while enterData == "y": 
        # Initialize Objects
        testCircuit1 = ResonantCircuit()    
        testCircuit2 = ParallelResonantCircuit()
        testCircuit3 = SeriesResonantCircuit()

        # INPUT - Collect Data - ensure float input
        while not done:
            try:       
                rf = float(input("Please enter the resonant frequency in radians per second."))
                b  = float(input("Please enter the bandwith."))
                k  = float(input("Please enter the gain at the resonant frequency"))
                done = True
            except ValueError:
                print("Invalid entry. Resetting questions.")
                continue

        # reset done for subsequent data sets
        done = False
        
        # Setter methods
        testCircuit1.setRF(rf)
        testCircuit1.setB(b)
        testCircuit1.setK(k)

        testCircuit2.setRF(rf)
        testCircuit2.setB(b)
        testCircuit2.setK(k)

        testCircuit3.setRF(rf)
        testCircuit3.setB(b)
        testCircuit3.setK(k)


        # PROCESS - Design Circuits
        testCircuit2.designCircuit()
        testCircuit3.designCircuit()

        # OUTPUT - Display Methods
        print("\nTEST CIRCUIT 1")
        testCircuit1.display()

        print("\nTEST CIRCUIT 2")
        testCircuit2.display()

        print("\nTEST CIRCUIT 3")
        testCircuit3.display()

        # Check if user wants to enter another data set
        valid = False
        
        while not valid:
            enterData = input("Would you like to enter another circuit? y/n")
            if enterData != "y" and enterData != "n":
                print("Invalid entry. Please try again.")
                continue
            elif enterData == "y":
                valid = True
            else:
                valid = True
                print("Thank you for using the Resonant Circuit Design App! Have a nice day!\n*******************")
                
################################################################################################
#
# Function 2:   testCase2()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will create one object from the ParallelResonantCircuit subclass,
#               collect data from user, use the data to set the values for the instance variables,
#               design the circuit, then display the description of the resonant frequency response
#               and the circuit design values. This function will only run once.
#
################################################################################################

def testCase2():
    
    print("Test Case 2 - Parallel Resonant Circuit Subclass")
    
    #### VARIABLES ####
    rf = 0                  # Float - Resonant Frequency     
    b = 0                   # Float - Bandwidth
    k = 0                   # Float - Gain at RF 
    done = False            # Bool  - While loop control
    
    # Initialize object
    testCircuit = ParallelResonantCircuit()

    # INPUT - Collect Data - ensure float input
    print("Please enter the following values to design a parallel resonant circuit:")
    while not done:
        try:
            rf = float(input("Please enter the resonant frequency in radians per second."))
            b  = float(input("Please enter the bandwith."))
            k  = float(input("Please enter the gain at the resonant frequency"))
            done = True
        except ValueError:
            print("Invalid entry. Resetting questions.")
            continue
    # Setter Methods
    testCircuit.setRF(rf)
    testCircuit.setB(b)
    testCircuit.setK(k)

    # PROCESS - Design Method
    testCircuit.designCircuit()
    
    # OUTPUT - Display Method 
    testCircuit.display()
    
    print("Thank you for using the Parallel Resonant Circuit Design App! Have a nice day!\n*******************")

############################# FUNCTION DEFINITIONS ############################################
#
# Function 3:   testCase3()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will create one object from the SeriesResonantCircuit subclass,
#               collect data from user, use the data to set the values for the instance variables,
#               design the circuit, then display the description of the resonant frequency response
#               and the circuit design values. This function will only run once.
#
################################################################################################

def testCase3():
 
    print("Test Case 3 - Series Resonant Circuit Subclass")

    #### VARIABLES ####
    rf = 0                  # Float - Resonant Frequency     
    b = 0                   # Float - Bandwidth
    k = 0                   # Float - Gain at RF
    done = False            # Bool  - While loop control
    
    # Initialize object
    testCircuit = SeriesResonantCircuit()

    # INPUT - Collect Data - ensure float input
    print("Please enter the following values to design a parallel resonant circuit:")
    while not done:
        try:
            rf = float(input("Please enter the resonant frequency in radians per second."))
            b  = float(input("Please enter the bandwith."))
            k  = float(input("Please enter the gain at the resonant frequency"))
            done = True
        except ValueError:
            print("Invalid entry. Resetting questions.")
            continue

    # Setter Methods
    testCircuit.setRF(rf)
    testCircuit.setB(b)
    testCircuit.setK(k)
    
    # PROCESS - Design Method
    testCircuit.designCircuit()

    #OUTPUT - Display Method
    testCircuit.display()
    
    print("Thank you for using the Series Resonant Circuit Design App! Have a nice day!\n*******************")

############################################################################################################
#
# Function 4:   main()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will run all test functions 
#
###########################################################################################################
def main():
    testCase1()
    testCase2()
    testCase3()
    os.system("pause")
############################################################################################################
main()
    
