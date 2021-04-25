###################################################################################################
#
# Program:      Resonant Circuit Design
# Module:       parallelResonantCircuit.py
# Author:       Catherine Trujillo
# Course:       CSC 217-470
# Date:         7/07/2020
#
###################################################################################################
#
#
# Description:  This module defines/implements the subclass ParallelResonantCircuit, which extends
#               the class Resonant Circuit by adding a method to design the parallel circuit for
#               the given RFR values. It also overrides the superclasses display method to include
#               a print out of the design values:
#               -  self._R = Resistance
#               -  self._C = Capacitance
#               -  self._L = Inductance
#
############################## SUBCLASS METHODS LIST ##############################################
#
#   __init__(self)
#   designCircuit(self)
#   display(self)
#
############################## LIBRARIES AND MODULES ##############################################

from resonantCircuit import ResonantCircuit

############################## SUBCLASS DEFINITION ################################################

class ParallelResonantCircuit(ResonantCircuit):

############################## METHODS ############################################################
#
# Method:       __init__(self)
#
# Parameters:   self
# Return Value: ParallelResonantCircuit object
#
# Purpose:      SuperClass Constructor initializes fields for:
#               _rf = Resonant Frequency in rad/s
#               _b  = Bandwidth in rad/s
#               _k  = Gain at RF
#
#               SubClass Constructor initiliazes fields for:
#               _R = Resistance
#               _C = Capacitance
#               _L = Inductance
#
####################################################################################################
   
    def __init__(self):
        super().__init__()
        self._R = 0
        self._C = 0
        self._L = 0

####################################################################################################
#
# Method:       designCircuit(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      Retrieve data from superclass fields for use in design calculations. Set subclass
#               instance fields using design equations provided in textbook
#
####################################################################################################
    
    def designCircuit(self):

        # Retrive data from superclass fields for use in design calculations
        rf = super().getRF()
        b  = super().getB()
        k  = super().getK()

        # Set subclass instance fields using design equations provided in textbook
        self._R = k
        self._C = 1 / (b * self._R)
        self._L = 1 / ((rf ** 2) * self._C)       

####################################################################################################
#
# Method:       display(self)
#
# Parameters:   self
# Return Value: None
#
# Purpose:      This method extends the superclass display method to include a printout of the 
#               Parallel Resonant Circuit Design Values
#
####################################################################################################

    def display(self):
        # Include superclass display method
        super().display()

        # Add parallel Circuit Design
        print("PARALLEL CIRCUIT DESIGN")
        print("R = {}".format(self._R))
        print("C = {}".format(self._C))
        print("L = {} \n".format(self._L))

################################## END SUBCLASS ###################################################
        
