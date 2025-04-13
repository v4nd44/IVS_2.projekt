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
    return a + b


"""
@brief subtraction
@param a first number 
@param b second number 
@return the difference of two numbers
"""
def sub(a,b):
    return a - b


"""
@brief multiplication
@param a first number 
@param b second number 
@return the product of two numbers
"""
def mul(a,b):
    return a * b


"""
@brief division
@param a first number 
@param b second number 
@return the quotient of two numbers
@raises ValueError if division by zero is attempted
"""
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


"""
@brief exponentiation
@param a the number
@param b the exponent
@return the result of raising a to the power of b
"""
def power(a,b):
    return a**b


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
    return a**(1/b)


"""
@brief factorial
@param n the number
@return the factorial of n
@raises ValueError if n is negative
"""
def fact(n):
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)