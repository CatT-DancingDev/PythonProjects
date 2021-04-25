################################################################################################
#
# Program:      Blue Sky Corporation Test Program
# Module:       user.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         6/28/2020
#
################################################################################################
#
# Description:  This module defines/implements the class User and defines the methods for
#               Blue Sky Corporation's loyalty rewards discount program.
#
############################## CLASS METHODS LIST ###############################################
#
#   __init__(self,new)
#   setName(self)
#   setID(self)
#   setEmailAddress(self)
#   setAmtBeforeDiscount(self, amount)
#   displayUserInformation(self)
#   *****sellPurchase(self, amount)***** REQUIRED
#   *****totalDiscount(self)*****        REQUIRED
#   printReceipt(self, amount)
#   writeFile(self)
#
############################## MODULES AND LIBRARIES ###########################################

import sys
import os

############################## CLASS DEFINITION ################################################

class User :
    #### INSTANCE VARIABLES ####
    _name = ""
    _ID = ""
    _emailAddress = ""
    _salesAccum = 0.0
    _noOfDiscounts = 0
    _amtBeforeDiscount = 0.0
    _amtAfterDiscount = 0.0


############################## METHODS #########################################################
#
# Method:       __init__(self, bool)
#
# Parameters:   self, bool new
# Return Value: User object
#
# Purpose:      If new == True, a user object is created by getting instance values from input
#               Else, the user ID is obtained from input and used to open and read a file with
#               saved user data. Instance values are assigned from this file.
#
################################################################################################

    def __init__ (self, new):
        if new == True:
            ## set instance variables
            self.setName()
            self.setID()
            self.setEmailAddress()
            self._salesAccum = 0
            self._noOfDiscounts = 0
            self._amtBeforeDiscount = 0.0
            self._amtAfterDiscount = 0.0
        else:
            ## create and open valid, non-empty readFile
            while True:
                ID = input("Please enter your userID")
                fileName = ID + ".txt"

                if not os.path.exists(fileName):
                    print("A file with that ID does not exist. Please enter a valid ID")
                    continue
                
                fileSize = os.path.getsize(fileName)

                if fileSize == 0:
                    print("File is empty. Please contact customer service. Exiting program.")
                    sys.exit()

                readFile = open(fileName, "r")

                try:
                    ## set instance variables
                    self._name = readFile.readline().rstrip()
                    self._ID = readFile.readline().rstrip()
                    self._emailAddress = readFile.readline().rstrip()
                    self._salesAccum = float(readFile.readline())
                    self._noOfDiscounts = int(readFile.readline())
                    self._amtBeforeDiscount = 0.0
                    self._amtAfterDiscount = 0.0
                except ValueError:
                    print("There was a problem retrieivng your data. Please contact customer service.")
                    readFile.close()
                    sys.exit()
                readFile.close()
                break
            
###################################################################################################
#
# Method:       setName(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      Set self._name according to user input. Ensure input is all alphabetical.
#
####################################################################################################

    def setName(self):
        valid = False

        # Ensure input is all alphabetical
        while not valid:
            name = input("Please enter your last name and first initial as one word.")
            if not name.isalpha():
                print("Only use alphabetic characters please.\n")
                continue
            valid = True
            
        self._name = name
        
####################################################################################################
#
# Method:       setID(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      Set self._ID according to user input. Ensure ID is 4-digit string. Ensure that ID is
#               not already in use.
#
####################################################################################################

    def setID(self):      
        valid = False
        
        while not valid:
            # Ensure ID is 4-digit string
            ID = input("Please enter a 4-digit number to create your user ID")
            if not ID.isdigit() or len(ID) != 4:
                print("\nInvalid entry. Please try again. \n")
                continue

            # Ensure ID is not already in use by checking if file with path ID + ."txt" exists
            fileName = ID + ".txt"
            if os.path.exists(fileName):
                print("\nThat ID is already taken. Please try again.\n")
                continue
            valid = True

        self._ID = ID
        
####################################################################################################
#
# Method:       setEmailAddress(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      Set self._emailAddress according to user input
#
####################################################################################################

    def setEmailAddress(self):
        self._emailAddress = self._name + self._ID + "@BlueSkyCorp.com"
        
####################################################################################################
#
# Method:       setAmtBeforeDiscount(self, amount)
#
# Parameters:   self, float amount
# Return Value: None
#
# Purpose:      Set self._amtBeforeDiscount to amount parameter
#
####################################################################################################

    def setAmtBeforeDiscount(self, amount):
        self._amtBeforeDiscount = amount

####################################################################################################
#
# Method:       displayUserInformation(self)
#
# Parameters:   self
# Return Value: None 
#
# Purpose:      Output instance fields to console screen
#
####################################################################################################

    def displayUserInformation(self):
        print("Name: " + self._name)
        print("User ID: " + self._ID)
        print("Email Address: " + self._emailAddress + "\n")
        print("Current Accumulated Sales (next discount at $200): $%.2f" % self._salesAccum)
        print("Number of discounts available: ", self._noOfDiscounts)
        
####################################################################################################
#
# Method:       sellPurchase(self, amount)
#
# Parameters:   self, float amount
# Return Value: None
#
# Purpose:      Complete the sale and calculate discount points and balance forward for user object,
#               print receipt for customer, and store data to file.
#
####################################################################################################    
            
    def sellPurchase(self, amount):
        
        ROLLOVER = 200      # Constant value for discount rewards

        # If sale not a positive integer greater than zero, return from function
        if self._amtBeforeDiscount <= 0:
            print("Sale amount must be greater than zero. Exiting method.")
            return

        # PROCESS
        self._amtAfterDiscount = self._amtBeforeDiscount - amount                   # Calculate amount after discount 
        totalSales = self._amtAfterDiscount + self._salesAccum                      # Calculate totalSales                       
        self._noOfDiscounts = int(self._noOfDiscounts + (totalSales // ROLLOVER))   # Calulate number of discounts
        self._salesAccum = totalSales % ROLLOVER                                    # Calculate sales rolled over

        # OUTPUT TO CONSOLE AND FILE
        self.printReceipt(amount)                                                                               
        self.writeFile()
        
####################################################################################################
#
# Method:       totalDiscount(self)
#
# Parameters:   self
# Return Value: discount amount
#
# Purpose:      Calculate and return the amount of discount to be applied to sale.
#               Only one discount can be used per sale.
#
####################################################################################################

    def totalDiscount(self):
        
        discountAmount = 10             # Discount is 10%

        # PROCESS - if user has discounts on file, calcualte discount amount based on self._amtBeforeDiscount
        if self._noOfDiscounts > 0: 
            discount = self._amtBeforeDiscount / discountAmount
            self._noOfDiscounts -= 1    # decrement _noOfDiscounts
        else:
            discount = 0

        # Return Value 
        return discount
    
####################################################################################################
#
# Method:       printReceipt(self, amount)
#
# Parameters:   self, float amount
# Return Value: None
#
# Purpose:      Output the receipt for sale
#
####################################################################################################

    def printReceipt(self, amount):
        print("Price before discount: $%.2f" % self._amtBeforeDiscount)
        print("Discount Amount This Sale: $%.2f" % amount)
        print("Total Price after discount: $%.2f" % self._amtAfterDiscount + "\n")
        print("Discounts accrued: ", self._noOfDiscounts)
        print("Amount Carried Forward (Next discount at $200): $%.2f" % self._salesAccum)

####################################################################################################
#
# Method:       writeFile(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      Open and write instance data to file
#
####################################################################################################

    def writeFile(self):
        # open writeFile 
        fileName = self._ID + ".txt"
        writeFile = open(fileName, "w")

        # write data to file
        writeFile.write(self._name + "\n")
        writeFile.write(self._ID + "\n")
        writeFile.write(self._emailAddress + "\n")
        writeFile.write(str(self._salesAccum) + "\n")
        writeFile.write(str(self._noOfDiscounts) + "\n")

        # close writeFile
        writeFile.close()

        # OUTPUT - Confirmation to console
        print("File saved to: " + fileName)

########################### END CLASS ###################################################################        


        
        

        
        

    
