###############################################################################################
#
# Program:      Blue Sky Corporation Test Program
# Module:       main.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         6/28/2020
#
###############################################################################################
#
# Description:  This main test program will test the classes User and Email. For each test
#               the program will check if the user is a new user, or existing. For the
#               loyalty rewards testSale, the program will allow user to continue entering
#               as many sales as they wish. Upon conclusion of the sales Test, the email test
#               will begin.
#
############################# MAIN PROGRAM FUNCTION LIST ######################################
#
# Function 1:   testSale()
# Function 2:   emailTest()
# Function 3:   main()
#
############################# MODULES AND LIBRARIES ###########################################
#
from email import Email
from user import User
#
############################# FUNCTION DEFINITIONS ############################################
#
# Function 1:   testSale()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose: This function will create a new or existing User object to calculate sales and loyalty
#          rewards discounts. It will save the user data to a file.
#
################################################################################################
def testSale():
    ##### Variables ######
    sale = 0.0              # float to store current sale amount
    enterSale = "y"         # string to store user response to enter another sale
    valid = False           # boolean to determine if a response is valid
    new = False             # boolean to for User __init__ parameter
    
    
    print("\n Welcome to Blue Sky Corporation Loyalty Rewards Discount Calculator \n")

    # INPUT - Ask if user is a new or returning user. 
    while valid == False:
        answer = input("Are you a new user? y/n")
        if answer == "y" or answer == "Y":
            new = True
            valid = True
        elif answer == "n" or answer == "N":
            new = False
            valid = True
        else:
            print("Invalid input. Press enter to try again. ")
            
    # Pass boolean response to initialize User object.
    if new == True:
        user = User(True)
    else:
        user = User(False)

    # OUTPUT - Display user info    
    user.displayUserInformation()

    # PROCESS - Iteratively get sale amount, calulate discount, store data
    while enterSale == "y":
        try:
            
            # INPUT - Set Current Sale Amount
            sale = float(input("Please enter the amount of your current sale: $"))
            user.setAmtBeforeDiscount(sale)

            # Calculate discount, store data to file
            user.sellPurchase(user.totalDiscount())

            # Reset valid
            valid = False
            while valid == False:
                # INPUT - Ask if user wants to complete another sale
                enterSale = input("Would you like to enter another sale? y/n")

                if enterSale != "y" and enterSale != "n":               # If invalid response, try again
                    print("\nInvalid response. Please try again. \n")
                    continue
                elif enterSale == "n":                                  # If "n", print message and return from function
                    print("Have a nice day!")
                    return
                else:                                                   # If "y" repeat sales process
                    valid = True
        except ValueError:
            print("Incorrect data type. Please try again.\n")
            continue
                  
                    

#######################################################################################################################
#
# Function 2:   emailTest()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will create a new or existing User object to test the email class. The sender argument
#               for the email object will be retrieved from the User object, and the recipient email will come from
#               user input. The emailTest function will create the email, print the email in user-readable format, 
#               and print the email in a single evaluatable string format.  
#
#######################################################################################################################
    
def emailTest():
    #### VARIABLES ####
    valid = False                       # boolean to determine if a response is valid
    answer = ""                         # string to store user response
    new = False                         # boolean to for User __init__ parameter
    sender = ""                         # string to store email address of user
    recipient = ""                      # string to store recipient address
    
    print("\nWelcome to Blue Sky Corporation Email Service \n")

    # INPUT - Ask if user is new.
    while valid == False:
        answer = input("Are you a new user? y/n")
        if answer == "y" or answer == "Y":
            new = True
            valid = True
        elif answer == "n" or answer == "N":
            new = False
            valid = True
        else:
            print("Invalid input")

    # Pass boolean response to initialize User object
    if new == True:
        user = User(True)
    else:
        user = User(False)
        
    # PROCESS - Assign sender and INPUT recipient   
    # Check for validity of sender and recipient email addresses
    sender = user._emailAddress
    valid = False
    
    while valid == False:      
        if "@" in sender and "." in sender and sender.find("@") + 1 < sender.find("."):
            valid = True
        else:
            sender = input("Please enter your email address. Must be in valid email format.\n")
            
    valid = False
    while valid == False:
        recipient = input("Please enter recipient email address: ")
        if "@" in recipient and "." in recipient and recipient.find("@") + 1 < recipient.find("."):
            valid = True
        else:
            print("Please enter a valid email address format.\n")

    # Create and print email object 
    email = Email(sender, recipient)

    # OUTPUT 
    email.printEmail()
    email.toString()
#################################################################################################################################
#
# Function 3:   main()
#
# Parameters:   noArgs
# Return Type:  None
#
# Purpose:      This function will run testSale() and emailTest()  
#
##################################################################################################################################
def main():
    testSale()
    emailTest()
##################################################################################################################################
main()
    


