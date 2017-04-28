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
volM = ['m^3','meter^3','meters^3','cubic meter','cubic meters','cubicmeter','cubicmeters']
volL = ["l", "liter", "liters", "litre", "litres"]
volCm = ['cm^3','centimeter^3','centimeters^3','cubic centimeter','cubic centimeters','cubiccentimeter','cubiccentimeters']
volMm = ['mL','ml','miliLiter','miliLiters','mililiter','mililiters']
volFt = ["ft^3", "ft3", "feet^3", "foot cubed", "feet cubed", "cubic foot", "cubic feet"]
volIgal = ['imperial gallons','imperialgallons','igal','IGal','Igal','iGal']
volGal = ["gal", "gals", "gallon", "gallons"]
volQt = ["qt", "qts", "quart", "quarts"]
volIn = ['in^3','inches^3','cubic inch','cubicinch','cubic inches','cubicinches']
volumeUnits = volM + volL + volCm + volMm + volFt + volIgal + volGal + volQt + volIn

# Definitions for units of force
forceN = ["n", "newton", "newtons", ]
forceKg = ["kg*m/s^2"]
forceDynes = ["dynes", "dyne"]
forceG = ["g*cm/s^2"]
forceLbf = ["lbf", "pound-force", "pounds-force", "pound force", "pounds force"]
forceLbm = ["lbm*ft/s^2"]
forceUnits = forceN + forceKg + forceDynes + forceG + forceLbf + forceLbm

# Definitions for units of pressure
pressAtm = ["atm", "atms", "atmophere", "atmospheres"]
pressPa = ["N/m^2", "pa", "pas", "pascal", "pascals"]
pressKpa = ['kpa','kilopascal','kilopascals']
pressBar = ["bar", "bars"]
pressD = ['dynes/cm^2','dyne/cm^2']
pressMmHg = ["mmhg", "mm hg", "torr", "milimeters of mercury"]
pressMh2o = ["m h2o", "mh2o", "meter of water", "meters of water"]
pressPsi = ["psi", "lb/in^2", "lbs/in^2"]
pressFth2o = ["ft h2o", "fth2o", "foot of water", "feet of water"]
pressInhg = ["in hg", "in. hg", "inhg", "inch of mercury", "inches of mercury"]
pressUnits = pressAtm + pressPa + pressKpa + pressBar + pressD + pressMmHg + pressMh2o + pressPsi + pressFth2o + pressInhg

# Definitions for units of energy
energyJ = ["j", "js", "joule", "joules", "n*m"]
energyErg = ["erg", "ergs", "dyne*cm"]
energyKj = ["kj", "kilojoule", "kilojoules"]
energyKwhr = ["kwhr", "kwhrs", "kw*hr", "kw*hrs", "kilowatt hour", "kw hr", "kw hour", "kilowatt hr"]
energyCal = ["cal", "cals", "calories", "calorie"]
energyFtlbf = ["ftlbf", "ft*lbf", "foot pound", "ft pound", "foot pounds", "ft pounds", "ft-lbf"]
energyBtu = ["btu", "btus", "british thermal unit", "british thermal units"]
energyUnits = energyJ + energyErg + energyKj + energyKwhr + energyCal + energyFtlbf + energyBtu

# Definitions for units of power
powerW = ["w", "watt", "watts", "j/s"]
powerCal = ["cal/s", "calories/second"]
powerFt = ['ft*lbf/s','foot pounds/second','foot pounds/s','ft pounds/s','ft pounds/second']
powerBtu = ['btu/s','british thermal units/second','british thermal units/second','british Thermal units/s']
powerHp = ["hp", "horsepower", "horse power"]
powerUnits = powerW + powerCal + powerFt + powerBtu + powerHp

# Definitions for units of Temperature
tempK = ['k', 'kelvin']
tempC = ['c', 'celcius']
tempF = ['f', 'farenheit']
tempR = ['r', 'rankine']
tempUnits = tempK + tempC + tempF + tempR

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
def length(number, given, desired):
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
def volume(number, given, desired):
    if given in volM:
        base = number
    elif given in volL:
        base = number/1000
    elif given in volCm:
        base = number/(10E6)
    elif given in volMm:
        base = number/(10E6)
    elif given in volFt:
        base = number/35.3146667215
    elif given in volIgal:
        base = number/219.969248299
    elif given in volGal:
        base = number/264.172051242
    elif given in volQt:
        base = (number/4)/264.172051242
    elif given in volIn:
        base = (number/1728)/35.3146667215
    else:
        base = "error"
    if desired in volM:
        final = base
    elif desired in volL:
        final = base*1000
    elif desired in volCm:
        final = base*(10E6)
    elif desired in volMm:
        final = base*(10E6)
    elif desired in volFt:
        final = base*35.3146667215
    elif desired in volIgal:
        final = base*219.969248299
    elif desired in volGal:
        final = base*264.172051242
    elif desired in volQt:
        final = (base*264.172051242)*4
    elif desired in volIn:
        final = (base*35.3146667215)*1728
    else:
        final = "error"
    return final

# Conversions for force
def force(number, given, desired):
    if given in forceN:
        base = number
    elif given in forceKg:
        base = number
    elif given in forceDynes:
        base = number/(10E5)
    elif given in forceG:
        base = number/(10E5)
    elif given in forceLbf:
        base = number/0.22480894244323335
    elif given in forceLbm:
        base = (number/32.174)/0.22480894244323335
    else:
        base = "error"
    if desired in forceN:
        final = base
    elif desired in forceKg:
        final = base
    elif desired in forceDynes:
        final = base*(10E5)
    elif desired in forceG:
        final = base*(10E5)
    elif desired in forceLbf:
        final = base*0.22480894244323335
    elif desired in forceLbm:
        final = (base*32.174)*0.22480894244323335
    else:
        final = "error"
    return final

# Conversions for pressure
def pressure(number, given, desired):
    if given in pressAtm:
        base = number
    elif given in pressPa:
        base = number/101325.01
    elif given in pressKpa:
        base = number/101.32501
    elif given in pressBar:
        base = number/1.0132501
    elif given in pressD:
        base = number/1013250.1
    elif given in pressMmHg:
        base = number/759.999952
    elif given in pressMh2o:
        base = number/10.332275548
    elif given in pressPsi:
        base = number/14.695950254
    elif given in pressInhg:
        base = number/29.9212583
    elif given in pressFth2o:
        base = number/33.89854205
    else:
        base = "error"
    if desired in pressAtm:
        final = base
    elif desired in pressPa:
        final = base*101325.01
    elif desired in pressKpa:
        final = base*101.32501
    elif desired in pressBar:
        final = base*1.0132501
    elif desired in pressD:
        final = base*1013250.1
    elif desired in pressMmHg:
        final = base*759.999952
    elif desired in pressMh2o:
        final = base*10.332275548
    elif desired in pressPsi:
        final = base*14.695950254
    elif desired in pressInhg:
        final = base*29.9212583
    elif desired in pressFth2o:
        final = base*33.89854205
    else:
        final = "error"
    return final

# Conversions for energy
def energy(number, given, desired):
    if given in energyJ:
        base = number
    elif given in energyErg:
        base = number/10000000
    elif given in energyKj:
        base = number/.001
    elif given in energyKwhr:
        base = number/(2.777777777778E-7)
    elif given in energyCal:
        base = number/0.2388458966275
    elif given in energyFtlbf:
        base = number/0.7375621492773
    elif given in energyBtu:
        base = number/0.0009478169879134
    else:
        base = "error"
    if desired in energyJ:
        final = base
    elif desired in energyErg:
        final = base*10000000
    elif desired in energyKj:
        final = base*.001
    elif desired in energyKwhr:
        final = base*(2.777777777778E-7)
    elif desired in energyCal:
        final = base*0.2388458966275
    elif desired in energyFtlbf:
        final = base*0.7375621492773
    elif desired in energyBtu:
        final = base*0.0009478169879134
    else:
        final = "error"
    return final

# Conversions for power
def power(number, given, desired):
    if given in powerW:
        base = number
    elif given in powerCal:
        base = number/0.2388458966275
    elif given in powerFt:
        base = number/0.7375621492773
    elif given in powerBtu:
        base = number/0.0009478169879134
    elif given in powerHp:
        base = number/0.001341022089595
    else:
        base = "error"
    if desired in powerW:
        final = base
    elif desired in powerCal:
        final = base*0.2388458966275
    elif desired in powerFt:
        final = base*0.7375621492773
    elif desired in powerBtu:
        final = base*0.0009478169879134
    elif desired in powerHp:
        final = base*0.001341022089595
    else:
        final = "error"
    return final

# Conversions for temperature
def temp(number, given, desired):
    if given in tempK:
        base = number
    elif given in tempC:
        base = number + 273.15
    elif given in tempR:
        base = number * 5/9
    elif base in tempF:
        base = (number + 459.67) * (5/9)
    else:
        base = 'error'
    if desired in tempK:
        final = base
    elif desired in tempC:
        final = base - 273.15
    elif desired in tempR:
        final = base * (9/5)
    elif desired in tempF:
        final = base * (9/5) - 459.67
    else:
        final = 'error'
    return final

def convert(value, unitsInitial, unitsFinal):
    # This function combine the above functions to allow for simpler use.
    unitsInitial=unitsInitial.lower()
    unitsFinal=unitsFinal.lower()
    if (unitsInitial in massUnits):
        convertedVal = mass(value, unitsInitial, unitsFinal)
    elif (unitsInitial in lengthUnits):
        convertedVal = length(value, unitsInitial, unitsFinal)
    elif (unitsInitial in volumeUnits):
        convertedVal = volume(value, unitsInitial, unitsFinal)
    elif (unitsInitial in forceUnits):
        convertedVal = force(value, unitsInitial, unitsFinal)
    elif (unitsInitial in pressUnits):
        convertedVal = pressure(value, unitsInitial, unitsFinal)
    elif (unitsInitial in energyUnits):
        convertedVal = energy(value, unitsInitial, unitsFinal)
    elif (unitsInitial in powerUnits):
        convertedVal = power(value, unitsInitial, unitsFinal)
    elif (unitsInitial in tempUnits):
        convertedVal = temp(value, unitsInitial, unitsFinal)
    else:
        print("Error. UnitConv does not recognize '" + unitsInitial+ "' as input units.")
    return convertedVal
