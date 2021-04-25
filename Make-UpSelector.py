########################################################################################################################################################
#
# Program Name: Pre-Test for CSC 217-470
# Programmer: Catherine Trujillo
# Date Created: 6/12/2020
# Date of Final Update: 6/14/2020
#
#########################################################################################################################################################
#
# Program description: This pre-test is to demonstrate my current knowledge of the Python Programming language. It will contain a function of my choosing
#                      that demonstrates the following standards:
#                                 - User Input
#                                 - Arithmetic and Variables
#                                 - If and nested-if statements
#                                 - For and while loops
#                                 - Strings
#                                 - Tuples
#                                 - Dictionaries/Lists
#                                 - Files/Exceptions
#                       The program will also contain a function to perform various computations on user input integers. The functions will be called from
#                       a main program driver.
#
###########################################################################################################################################################

import os.path          # Used for fileName verification
from os import path     # Used for fileName verification

############################################################################################################################################################
# Function: makeupApp()
# Args:     no-args
# return:   no return value
#
# Purpose: The makeup app will help you choose a coordinated color palette, giving you color-combination tips along the way, print your receipt, and save
#          your choices to an external file, making sure to check for common file exceptions. You will also be given the option to make a separate copy of
#          the file externally.
############################################################################################################################################################

def makeupApp() :
    
    ############ DATA AND VARIABLES ###############

    total_price = 0         # Int variable used to tally the total price
    user_name = ""          # String variable used for file creation, and personalization in the app
    file_name = ""          # String variable used to check for file name validity
    new_name = ""           # String variable used if file_name already exists 
    response = ""           # String variable to store user's yes/no selections

    eyeshadow_choice = ""   # String variable to store user's choice
    blush_choice = ""       # String variable to store user's choice
    lipstick_choice = ""    # String variable to store user's choice

    valid_entry = False     # Used to terminate while loop that forces valid user input

    
    makeup = ("EYESHADOW", "BLUSH", "LIPSTICK")     # TUPLE to define makeup types

    
    eyeshadow = {"warm" : "copper", "cool" : "violet", "neutral" : "sable"}     # DICTIONARIES for each make-up item.
    blush = {"warm" : "coral", "cool" : "berry", "neutral" : "tawny"}           #      color temperature: color name 
    lipstick = {"warm" : "crimson", "cool" : "merlot", "neutral" : "nude"}
    
    price = {"eyeshadow" : 9.95, "blush" : 7.49, "lipstick" : 10.99 }           # DICTIONARY for pricing items - type : price 
    

    
    ################### PROCESS #######################
    
    # Welcome and Description
    print("********* Welcome to the Makeup App **********\n\nCreate your own personalized color palette!\n")

    # INPUT - user_name
    user_name = input("Let's start with introductions. What's your name? ") 

    print("\nHello " + user_name + ". Let's start creating!")
    print ("Make your selections from the table below: \n \n")

    # OUTPUT - Selections Table 
    print("              WARM" + "         COOL" + "        NEUTRAL        " + "PRICE \n")
    print(makeup[0] + "    " + eyeshadow["warm"] + "       " + eyeshadow["cool"] + "       " + eyeshadow["neutral"] + "         " , price["eyeshadow"])
    print(makeup[1] + "        " + blush["warm"] + "        " + blush["cool"] + "        " + blush["neutral"] + "         " , price["blush"])
    print(makeup[2] + "     " + lipstick["warm"] + "      " + lipstick["cool"] + "       " + lipstick["neutral"] + "          " , price["lipstick"])


    # WHILE LOOP with IF STATEMENT - Force valid user entry for eyeshadow selection 
    while valid_entry == False:
        eyeshadow_choice = input("\nChoose an eyeshadow color from the table above. ")
        if eyeshadow_choice == "copper" or eyeshadow_choice == "violet" or eyeshadow_choice == "sable":
            valid_entry = True
    
    # IF/ELIF/ELSE STATEMENT - Use eyeshadow_choice as value for reverse key look-up to determine if their selection is warm, cool, or neutral
    if list(eyeshadow.keys())[list(eyeshadow.values()).index(eyeshadow_choice)] == "warm":
        print("\nColor Palette Tip: Warm eyeshadows like copper go great with a neutral blush and warm lipstick.")
    elif list(eyeshadow.keys())[list(eyeshadow.values()).index(eyeshadow_choice)] == "cool":
        print("\nColor Palette Tip: Cool eyeshadows like violet go great with a cool blush and neutral lipstick.")
    else:
        print("\nColor Palette Tip: Neutral eyeshadows like sable go great with just about any combination of blush and lipstick.")


    valid_entry = False     # Reset valid_entry

    # WHILE LOOP with IF STATEMENT - Force valid user entry for blush selection
    while valid_entry == False:    
        blush_choice = input("Choose a blush color from the table above. ")
        if blush_choice == "coral" or blush_choice == "berry" or blush_choice == "tawny":
            valid_entry = True

    # NESTED-IF STATEMENTS to give personalized color-matching tips. Outer statements refer to blush temperature. Inner statements refer to eyeshadow temperature.
    if blush_choice == blush["warm"]:
        if eyeshadow_choice == eyeshadow["warm"]:
            print("\nColor Palette Tip: Warm colors go great with other warm colors or neutrals. We recommend crimson for your lipstick color.")
        elif eyeshadow_choice == eyeshadow["cool"]:
            print("\nColor Palette Tip: Mixing warm and cool tones makes a bold statement. We recommend nude lipstick for a great day look or crimson lipstick for a sassy evening look.")
        else:
            print("\nColor Palette Tip: Warm blush with neutral eyeshadow really shows off your cheek bones. Complement the look without going overboard by choosing a neutral lipstick.")

    elif blush_choice == blush["cool"]:
        if eyeshadow_choice == eyeshadow["warm"]:
            print("\nColor Palette Tip: Copper eyeshadow with berry blush is a playful combo. Complete the look with merlot lipstick to really show off your zest for life!")
        elif eyeshadow_choice == eyeshadow["cool"]:
            print("\nColor Palette Tip: Violet eyeshadow with berry-hued  blush creates a classically romantic look. Keep the look soft with a nude lipstick, or up the intensity with a flirty merlot lipstick.")
        else:
            print("\nColor Palette Tip: Neutral eyeshadow and cool blush give you a look that's effortlessly chic. Nude lipstick really perfects the look! ")

    else:
        if eyeshadow_choice == eyeshadow["warm"]:
            print("\nColor Palette Tip: Copper eyeshadow takes the spotlight when combined with a neutral blush. Keep the focus on your gorgeous gazers by using a nude lipstick.")
        elif eyeshadow_choice == eyeshadow["cool"]:
            print("\nColor Palette Tip: Cool eyeshadow and neutral blush go great with a cool and complementary lipstick. We recommend merlot.")
        else:
            print("\nColor Palette Tip: Sable eyeshadow and tawny blush make the perfect playground for any lipstick choice! Go wild and have fun!")

    valid_entry = False     # Reset valid_entry

    # WHILE LOOP with IF STATEMENT - Force valid user entry for lipstick selection
    while valid_entry == False:    
        lipstick_choice = input("Choose a lipstick color from the table above. ")
        if lipstick_choice == "crimson" or lipstick_choice == "merlot" or lipstick_choice == "nude":
            valid_entry = True

    # INPUT - Does user want receipt displayed? 
    response = input("\nCongratulations! Your color palette is complete. Would you like to print your receipt? y/n")

    # OUTPUT FORMATTING and ARITHMETIC - Receipt     
    if response == "y":
        print("\n     ****************** RECEIPT ******************\n")
        total_price = total_price + price["eyeshadow"] + price["blush"] + price["lipstick"] # ARITHMETIC
        print("          " + eyeshadow_choice.upper() + " " + makeup[0] + "\n%30s" % "$"   , price["eyeshadow"])
        print("          " + blush_choice.upper() + " " + makeup[1] + "\n%30s" % "$", price["blush"])
        print("          " + lipstick_choice.upper() + " " + makeup[2] + "\n%30s" % "$"   , price["lipstick"])
        print("\n%30s" % "TOTAL:     $", total_price)
        print("\n     *********************************************\n")
    
    # FILE WRITING - DO NOT ALLOW TO OVERWRITE EXISITNG FILE
    file_name = user_name + ".txt"      # STRING CONCANTENATION

    # While loop to check if file already exists. If so, force entry of valid, unused name
    while path.exists(file_name):   
        print("\nDirectory Alert: A file with that user name already exists.")
        new_name = input("Please enter a new user name to save your Personalized Color Pallette.\n")
        file_name = new_name + ".txt"
        
    # WRITE PROCESS
    outfile = open(file_name, "w")
    outfile.write(user_name + "'s Personalized Color Pallette \n")
    outfile.write("Eyeshadow: " + eyeshadow_choice + "\n")
    outfile.write("Blush: " + blush_choice + "\n")
    outfile.write("Lipstick: " + lipstick_choice +"\n")
    outfile.close()
        
    # Alert user that file has been created. Display the file name.    
    print("\nYour Personalized Color Palette is saved to the following file: " + file_name)

    # INPUT - Does user want to copy file?
    response = input("\nWould you like to make a copy of your Personalized Color Pallette? y/n ")
    
    if response == "y":
        file_name_valid = False     # reset file_name_valid

        # FILE COPY
        while file_name_valid == False:
            try:
                # Get name of file to be copied
                file_name = input("\nPlease enter the original file name as it appears above.\n")

                # Open input file
                infile = open(file_name, "r")

                # Get name of copy file
                copy_file_name = input("\nPlease enter a different name for the copied file to be saved. Be sure to include '.txt'\n") 

                # RAISE EXCEPTIONS               
                if copy_file_name[-4:] != ".txt":       # Check for file type validity                                                       
                    raise IOError   
                if path.exists(copy_file_name):         # Check if file already exists
                    raise FileExistsError

                # Open output file
                outfile = open(copy_file_name, "w")

                # Copy File Line by Line 
                for i in range (0, 4):
                    line = infile.readline()
                    outfile.write(line)

                # Close Files
                infile.close()
                outfile.close()

                # Alert user of successful file creation
                print("\nCopy file '{}' successfully created.\n".format(copy_file_name))
                file_name_valid = True      # Exit loop

            # EXCEPTION HANDLING
            except FileNotFoundError:       # Input File entered incorrectly - restart copy protocol
                print("\nThat file was not found. Make sure to include '.txt' in the file name. Restarting copy protocol.")
            except FileExistsError:         # Output File already exists - restart copy protocol
                print("\nCopy File Name already exists. Restarting copy protocol.")
            except IOError:                 # Output file entered incorrectly - restart copy protocol
                print("\nInvalid file name. Please remember to include .txt in your file names. Restarting copy protocol.")

    # Salutations            
    print("\nThank you for using the Color Make-Up App! Have a Beautiful Day!\n")
    
################################################### End makeupApp() #######################################################################################

############################################################################################################################################################
# Function: integerFun()
# Args:     no-args
# return:   no return value
#
# Purpose: This function will take user input for 5 integers and output the minimum, maximum and mean
############################################################################################################################################################
    
def integerFun() :
    
    ############# VARIABLES #################
    integer = 0         # int variable used to store user input 
    minimum = 0         # int variable used to keep track of minimum int
    maximum = 0         # int variable used to keep track of maximum int
    total = 0           # int variable used to keep track of sum of integers
    mean = 0            # int variable used to store average of ints
    
    # WELCOME
    print("Welcome to integerFun!")

    # While loop to get 5 integers  
    i = 0
    while i < 5:
        # Input
        integer = int(input("Please enter an integer. "))
        # Calculations
        total = total + integer     # Add new value to running total

        if i == 0:                  # On first iteration, assign integer to minimum and maximum variable
            minimum = integer
            maximum = integer
            i = i + 1
            continue 
        if integer < minimum:       # On subsequent iterations, check if integer is <. 
            minimum = integer       #       If so, store in minimum

        if integer > maximum:       # If integer is > maximum, store in maximum
            maximum = integer
        i = i + 1
    mean = total / 5                # Calculate average

    # OUTPUT RESULTS
    print("Minimum: " , minimum)
    print("Maximum: " , maximum)
    print("Mean:    " , mean)
    
####################################### End integerFun() ###################################################################################################        

############################################################################################################################################################
# Function: main()
# Args:     no-args
# return:   no return value
#
# Purpose: main program driver. Calls all functions in program.
############################################################################################################################################################
def main() :
    makeupApp()                 # Call makeupApp
    integerFun()                # Call integerFun
########################################## End Main() ######################################################################################################
main()      # Run Program          
            
    

        
    
    




