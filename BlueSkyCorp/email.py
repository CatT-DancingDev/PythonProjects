###############################################################################################
#
# Program:      Blue Sky Corporation Test Program
# Module:       email.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         6/28/2020
#
###############################################################################################
#
# Description:  This module defines/implements the class Email and defines the methods for
#               Blue Sky Corporation's email formatter which has two outputs:
#                   - Standard format email
#                   - Single String format email
#
############################# MODULES AND LIBRARIES ###########################################
#
from user import User
from datetime import datetime
#
###############################################################################################

class Email :
    #### INSTANCE VARIABLES ####
    _date = ""
    _message = ""
    _sender = ""
    _recipient = ""
    _subject = ""
    
############################# CLASS METHODS LIST #################################################
#
#   __init__(self, sender, recipient)   REQUIRED
#   getSubject(self)
#   *****append(self)*****              REQUIRED
#   printEmail(self)
#   *****toString(self)*****            REQUIRED
#
##################################################################################################
#
# Method:       __init__(self, sender, recipient)
#
# Parameters:   self, string sender, string recipient
# Return Value: email object
#
# Purpose:      Create an email object 
#
##################################################################################################
    def __init__(self, sender, recipient) :
        self._sender = "Sender: " + sender
        self._recipient = "Recipient: " + recipient
        self._date = "Date: " + str(datetime.now())
        self.getSubject()
        self.append()

###################################################################################################
#
# Method:       getSubject(self)
#
# Parameters:   noArgs
# Return Value: None
#
# Purpose:      Assign self._subject according to input 
#
##################################################################################################        
    def getSubject(self):
        subject = input("Subject: ")
        self._subject = "Subject: " + subject

###################################################################################################
#
# Method:       append(self)
#
# Parameters:   noArgs
# Return Value: None
#
# Purpose:      Appends message strings line-by-line. User must type DONE to finish.  
#
################################################################################################     
    def append(self):
        # VARIABLES
        line = ""               # String to store single line of input
        message = "Message: "   # String to hold message

        # PROCESS - Ask user to type message
        print("Please type your message. When you are finished, type DONE on the last line and press enter : \n")

        # Read each line until "DONE" and append each line to message string
        while True:
            line = input()
            if line == "DONE":
                break
            message += line + "\n"
        # Assign instance variable
        self._message = message

################################################################################################
#
# Method:       printEmail(self)
#
# Parameters:   noArgs
# Return Value: None
#
# Purpose:      Prints contents of email in a standard email format.  
#
################################################################################################          
    def printEmail(self):
        print(self._sender + "\n")
        print(self._recipient + "\n")
        print(self._date + "\n")
        print(self._subject + "\n")
        print(self._message + "\n")

################################################################################################
#
# Method:       toString(self)
#
# Parameters:   noArgs
# Return Value: None
#
# Purpose:      Prints contents of email in a single representational string format. 
#
################################################################################################  
    def toString(self):
        # Add all instance values to message separated by \n
        message = self._sender + "\n" + self._recipient + "\n" + self._date + "\n" + self._subject + "\n" + self._message + "\n"

        # Create single evaluatable string 
        newMessage = repr(message)

        # OUTPUT - to console screen
        print(newMessage)
            
    


