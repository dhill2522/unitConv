# -*- coding: utf-8 -*-
"""
Created on Mar 16 2016

@author: dhill2522

Unit Conversions Library
"""
massKg = ["kg", "kilgrams", "kilogram", "kilos", "kilo"]
massG = ["g", "gram", "grams"]
massMton = ["metric ton"]
massLb = ["lb", "lbs", "pounds", "pound", "lbm"]
massOz = ["oz", "ounce", "ounces", "ozs"]
massTon = ["ton", "tons"]
massUnits = massKg + massG + massMton + massLb + massOz + massTon


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
