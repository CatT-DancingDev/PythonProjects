###############################################################################################
#
# Program:      Resonant Circuit Design
# Module:       resonantCircuit.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/07/2020
#
###############################################################################################
#
#
# Description:  This module defines/implements the superclass ResonantCircuit, which stores the
#               data needed to describe a resonant frequency response.  
#
############################## CLASS METHODS LIST #############################################
#
#   __init__(self)
#   setRF(self, rf)
#   setB(self, b)
#   setK(self, k)
#   getRF(self)
#   getB(self)
#   getK(self)
#   display(self)
#
############################## CLASS DEFINITION ################################################

class ResonantCircuit:
    
############################## METHODS #########################################################
#
# Method:       __init__(self)
#
# Parameters:   self
# Return Value: ResonantCircuit object
#
# Purpose:      Intantiate a ResonantCircuit Object with data fields for:
#               _rf = Resonant Frequency in rad/s
#               _b  = Bandwidth in rad/s
#               _k  = Gain at RF
#
#################################################################################################

    def __init__(self):
        self._rf = 0
        self._b = 0
        self._k = 0

#################################################################################################
#
# Method:       getRF(self)
#
# Parameters:   self
# Return Value: self._rf
#
# Purpose:      Returns the value of self._rf
#
#################################################################################################

    def getRF(self):
        return self._rf

#################################################################################################
#
# Method:       getB(self)
#
# Parameters:   self
# Return Value: self._b
#
# Purpose:      Returns the value of self._b
#
#################################################################################################

    def getB(self):
        return self._b

#################################################################################################
#
# Method:       getK(self)
#
# Parameters:   self
# Return Value: self._k
#
# Purpose:      Returns the value of self._k
#
#################################################################################################

    def getK(self):
        return self._k

#################################################################################################
#
# Method:       setRF(self, rf)
#
# Parameters:   self, float rf 
# Return Value: None
#
# Purpose:      Assigns the value of  rf to self._rf 
#
#################################################################################################

    def setRF(self, rf):
        self._rf = rf

#################################################################################################
#
# Method:       setB(self, b)
#
# Parameters:   self, float b 
# Return Value: None
#
# Purpose:      Assigns the value of b to self._b
#
#################################################################################################

    def setB(self, b):
        self._b = b

#################################################################################################
#
# Method:       setK(self, k)
#
# Parameters:   self, float k 
# Return Value: None
#
# Purpose:      Assigns the value of k to self._k 
#
#################################################################################################

    def setK(self, k):
        self._k = k

#################################################################################################
#
# Method:       display(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      Displays the description of the resonant frequency response
#
#################################################################################################

    def display(self):
        
        print("RESONANT FREQUENCY RESPONSE:")
        print("Resonant Frequency = {} rad/s".format(self._rf))
        print("Bandwidth = {} rad/s".format(self._b))
        print("Gain At Resonant Frequency = {} \n".format(self._k))
    
##################################### END CLASS ################################################# 
