# Problem 1: Basic functions -Greet
def greet(name):
    return f"hello,{name}! welcome to python"
# Test
print(greet("Jayendra "))
#Output:Hello, Jayendra !welcome to python


#  Problem 2: Add 2 Numbers
def add(a,b):
    return a+b
print(add(10,20))  # Output : 30


# Problem 3:Check Even or Odd
def is_even(num):
    if num % 2 ==0:
        return True
    else:
        return False 
print(is_even(4)) # True
print(is_even(7)) # False


#Problem 4:Max of 3 Numbers .
def max_of_three(a,b,c):
    if a >=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(max_of_three(10,25,15))   #  25


# Problem 5:Square Using loop and function .
def square_by_addition(n):
    square=0
    for i in range(n):
        square=square+n
    return square 
print (square_by_addition(4))   # 16
print(square_by_addition(5))#  25


# Problem 3:Factorial- Recursion Intro
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))   # 120


# Problem 7:Check whether Palindrome or not---string + function
def is_palindrome(word):
    word=word.lower()
    return word==word[::-1]
print(is_palindrome("Madam"))  # True
print(is_palindrome("Python"))  # False
