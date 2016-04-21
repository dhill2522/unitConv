# -*- coding: utf-8 -*-
"""
Created on Apr 19 2016

@author: dhill2522 & jshammon

Unit Conversions Library

Notes:
Should add support for centi, mili,...
Could branch unit definitions to an appendix file so they could also be used elsewhere
could also add cooking units like cups, tsp, Tbs...
Find a way of adding cross-dimension conversion eg. W --> J/s --> ft*lbf/s
could add mass/moles conversions as well
we may want to add an error function. in order to reduce repetition
"""
# Definitions for units of mass
massKg = ["kg", "kgs", "kilgrams", "kilogram", "kilos", "kilo"]
massG = ["g", "gs", "gram", "grams"]
massMton = ['mton','mtons','metric ton','metric tons','metricton','metrictons']
massLb = ["lb", "lbs", "pounds", "pound",'lbm', 'lbms','pound mass','pounds mass','poundmass','poundsmass']
massOz = ["oz", "ounce", "ounces", "ozs"]
massTon = ['ton','tons','uston','ustons','USton','UStons']
massUnits = massKg + massG + massMton + massLb + massOz + massTon

# Definitions for units of length
lengthM = ["m", "meter", "meters"]
lengthCm = ['cm','centimeter','centimeters']
lengthMm = ['mm','milimeter','milimeters']
lengthMicron = ['micron','microns','mcrn','mcrns','micrometer','micrometers']
lengthAng = ['angstrom','angstroms','A']
lengthIn = ["in", "inch", "inches"]
lengthFt = ["ft", "foot", "feet"]
lengthYd = ["yd", "yds", "yard", "yards"]
lengthMile = ["mi", "mil", "mile", "miles"]
lengthUnits = lengthM + lengthCm + lengthMm + lengthMicron + lengthAng + lengthIn + lengthFt + lengthYd + lengthMile

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
def mass(number, given, desired):
    # Convert given value to kg and then to the desired units
    if given in massKg:
        base = number
    elif given in massG:
        base = number/1000
    elif given in massMton:
        base = number/0.001
    elif given in massLb:
        base = number/2.20462247604
    elif given in massOz:
        base = number*35.27392
    elif given in massTon:
        base = (number*2000)/2.20462247604
    else:
        return "Error, initial units not recognized!"
    if desired in massKg:
        final = base
    elif desired in massG:
        final = base*1000
    elif desired in massMton:
        final = base*0.001
    elif desired in massLb:
        final = base*2.20462247604
    elif desired in massOz:
        final = base*35.27392
    elif desired in massTon:
        final = (base*2.20462247604)/2000
    else:
        return "Error, final units not recognized!"
    return final
# Conversions for length
def length(given,desired,number):
    if given in lengthM:
        base = number
    elif given in lengthCm:
        base = number/100
    elif given in lengthMm:
        base = number/1000
    elif given in lengthMicron:
        base = number/(10E6)
    elif given in lengthAng:
        base = number/(10E10)
    elif given in lengthIn:
        base = number/39.3700787402
    elif given in lengthFt:
        base = number/3.28083989501
    elif given in lengthYd:
        base = number/1.09361329834
    elif given in lengthMile:
        base = number/0.000621371192237
    else:
        return "Error, initial units not recognized!"
    if desired in lengthM:
        final = base
    elif desired in lengthCm:
        final = base*100
    elif desired in lengthMm:
        final = base*1000
    elif desired in lengthMicron:
        final = base*(10E6)
    elif desired in lengthAng:
        final = base*(10E10)
    elif desired in lengthIn:
        final = base*39.3700787402
    elif desired in lengthFt:
        final = base*3.28083989501
    elif desired in lengthYd:
        final = base*1.09361329834
    elif desired in lengthMile:
        final = base*0.000621371192237
    else:
        return "Error, final units not recognized!"
    return final

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
        convertedVal = mass(value, unitsInitial, unitsFinal)
    if (unitsInitial in lengthUnits):
        convertedVal = length(value, unitsInitial, unitsFinal)
    if (unitsInitial in volumeUnits):
        convertedVal = volume(value, unitsInitial, unitsFinal)
    if (unitsInitial in forceUnits):
        convertedVal = force(value, unitsInitial, unitsFinal)
    if (unitsInitial in pressUnits):
        convertedVal = press(value, unitsInitial, unitsFinal)
    if (unitsInitial in energyUnits):
        convertedVal = energy(value, unitsInitial, unitsFinal)
    if (unitsInitial in powerUnits):
        convertedVal = power(value, unitsInitial, unitsFinal)
