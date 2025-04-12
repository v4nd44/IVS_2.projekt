# IVS - 2. projekt
# matematická knihovna pro kalkulačku

"""
@brief scitani
@param a prvni cislo 
@param b druhe cislo 
@return soucet dvou cisel
"""
def add(a,b):   
    return a+b

"""
@brief odcitani
@param a prvni cislo 
@param b druhe cislo 
@return rozdil dvou cisel
"""
def subtract(a,b):
    return a-b

"""
@brief nasobeni
@param a prvni cislo 
@param b druhe cislo 
@return nasobek dvou cisel
"""
def multiply(a,b):
    return a*b

"""
@brief deleni
@param a prvni cislo 
@param b druhe cislo 
@return podil dvou cisel
"""
def devide(a,b):
    if b == 0:
        raise ValueError("Nelze dělit nulou.")
    return a / b