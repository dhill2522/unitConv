# -*- coding: utf-8 -*-
"""
Created on Mar 16 2016

@author: dhill2522

Unit Conversions Library

Notes:
Should add support for centi, mili,...
Could branch unit definitions to an appendix file so they could also be used elsewhere

"""
massKg = ["kg", "kilgrams", "kilogram", "kilos", "kilo"]
massG = ["g", "gram", "grams"]
massMton = ["metric ton"]
massLb = ["lb", "lbs", "pounds", "pound", "lbm"]
massOz = ["oz", "ounce", "ounces", "ozs"]
massTon = ["ton", "tons"]
massUnits = massKg + massG + massMton + massLb + massOz + massTon

# Definitions for units of length
lengthM = ["m", "meter", "meters"]
lengthIn = ["in", "inch", "inches"]
lengthFt = ["ft", "foot", "feet"]
lengthYd = ["yd", "yds", "yard", "yards"]
lengthMile = ["mi", "mil", "mile", "miles"]
lengthUnits = lengthM + lengthIn + lengthFt + lengthYd + lengthMile

# Conversions for mass
def mass(value, unitsInitial, unitsFinal):
    # Convert given value to kg and then to the desired units
    if (unitsInitial in massKg):
        x=0



def convert(value, unitsInitial, unitsFinal):
    # This function combine the above functions to allow for simpler use.
    unitsInitial=unitsInitial.lower()
    unitsFinal=unitsFinal.lower()
    if (unitsInitial in massUnits):
        x=0


print (massUnits)
