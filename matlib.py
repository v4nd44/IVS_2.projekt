# IVS - 2. projekt
# matematická knihovna pro kalkulačku

# autor: Klara Luskacova (xluskak00)
# tym: vydrysek

"""
@brief addition
@param a first number 
@param b second number 
@return the sum of two numbers
"""
def add(a,b):   
    return round(a + b, 13)


"""
@brief subtraction
@param a first number 
@param b second number 
@return the difference of two numbers
"""
def sub(a,b):
    return round(a - b, 13)

"""
@brief multiplication
@param a first number 
@param b second number 
@return the product of two numbers
"""
def mul(a,b):
    return round(a * b, 13)


"""
@brief division
@param a first number 
@param b second number 
@return the quotient of two numbers
@raises ZeroDivisionError if division by zero is attempted
"""
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return round(a / b, 13)


"""
@brief exponentiation
@param a the number
@param b the exponent
@return the result of raising a to the power of b
"""
def power(a,b):
    if a == 0 and b == 0:
        raise ValueError
    if b <= 0:
        raise ValueError
    if a < 0 and not float(b).is_integer():
        raise ValueError
    return round(a ** b, 13)


"""
@brief root
@param a the number
@param b the degree of the root
@return the b-th root of a
@raises ValueError if a is negative and b is even.
"""
def sqrt(a,b):
    if a<0 and b % 2 == 0:
        raise ValueError
    if b==0:
        return ValueError
    return round(a ** (1 / b), 13)


"""
@brief factorial
@param n the number
@return the factorial of n
@raises ValueError if n is negative
"""
def fact(n):
    if not isinstance(n, int):
        raise ValueError
    if n<0:
        raise ValueError
    result = 1
    for idx in range(2, n + 1):
        result = result * idx
    return round(result, 13)