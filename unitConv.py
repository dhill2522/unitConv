# -*- coding: utf-8 -*-
"""
Created on Mar 16 2016

@author: dhill2522 & jshammon

Unit Conversions Library

Notes:
Should add support for centi, mili,...
Could branch unit definitions to an appendix file so they could also be used elsewhere
could also add cooking units like cups, tsp, Tbs...
Find a way of adding cross-dimension conversion eg. W --> J/s --> ft*lbf/s
"""
# Definitions for units of mass
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

# Definitions for units of volume
volM = ["m^3", "m3", "meters cubed", "meter cubed", "cubic meters", "cubic meter"]
volL = ["l", "liter", "liters", "litre", "litres"]
volFt = ["ft^3", "ft3", "foot cubed", "feet cubed", "cubic foot", "cubic feet"]
volGal = ["gal", "gals", "gallon", "gallons"]
volQt = ["qt", "qts", "quart", "quarts"]
volUnits = volM + volL + volFt + volGal + volQt

# Definitions for units of force
forceN = ["n", "newton", "newtons"]
forceDynes = ["dynes", "dyne"]
forceLbf = ["lbf", "pound-force", "pounds-force"]
forceUnits = forceN + forceDynes + forceLbf

# Definitions for units of pressure
pressAtm = ["atm", "atms", "atmophere", "atmospheres"]
pressPa = ["pa", "pas", "pascal", "pascals"]
pressBar = ["bar"]
pressMmHg = ["mmhg", "milimeters of mercury"]
pressTorr = ["torr"]
pressMh2o = ["m h2o", "mh2o", "meter of water", "meters of water"]
pressPsi = ["psi", "lb/in^2", "lbs/in^2"]
pressFth2o = ["ft h2o", "fth2o", "foot of water", "feet of water"]
pressInhg = ["in hg", "in. hg", "inch of mercury", "inches of mercury"]
pressUnits = pressAtm + pressPa + pressBar + pressMmHg + pressTorr + pressMh2o + pressPsi + pressFth2o + pressInhg

# Definitions for units of energy
energyJ = ["j", "js", "joule", "joules"]
energyErg = ["erg", "ergs"]
energyKwhr = ["kwhr", "kwhrs", "kw*hr", "kw*hrs"]
energyCal = ["cal", "cals", "calories", "calorie"]
energyFtlbf = ["ftlbf", "ft*lbf"]
energyBtu = ["btu", "btus"]
energyUnits = energyJ + energyErg + energyKwhr + energyCal + energyFtlbf + energyBtu

# Definitions for units of power
powerW = ["w", "watt", "watts"]
powerHp = ["hp", "horsepower"]
powerUnits = powerW + powerHp

# Conversions for mass
def mass(value, unitsInitial, unitsFinal):
    # Convert given value to kg and then to the desired units
    if (unitsInitial in massKg):
        x=0
# Conversions for length
# Conversions for volume
# Conversions for force
# Conversions for pressure
# Conversions for energy
# Conversions for power


def convert(value, unitsInitial, unitsFinal):
    # This function combine the above functions to allow for simpler use.
    unitsInitial=unitsInitial.lower()
    unitsFinal=unitsFinal.lower()
    if (unitsInitial in massUnits):
        x=0
        # send to mass
