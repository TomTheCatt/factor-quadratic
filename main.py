#Intro
print("Quadratic equation factoring tool!")
print("Loading. . .")

import time
import math
from fractions import Fraction

equation, space_length = 0, 18

class other_math:
    def square(num: int):
        result = num*num
        return result
    def simply_fraction(numerator: int, denominator: int):
        pass

#quadratic equation facotring function
def factor_quadratic(a: int, b: int, c: int):
    if int(a) != 1:
        return quadratic_formula(a, b, c)
    value_to_return = None
    a_c = a*c
    print(f"{a} * {b} = {a_c}")
    #Checks the positives
    for i in range(abs(a_c)):
        try:
            result = a_c/i
            factor = result+i
            if bool((result).is_integer()) != False:
                first, second = f"{a_c} / {i} =  {int(result)}", f"{int(result)} + {i} = {factor}"
                first_length, second_length = " "*(space_length-len(first)), " "*(space_length-len(second))
                print(f"{a_c} / {i} = {int(result)} {first_length} ||| {second_length} {int(result)} + {i} = {int(factor)}")
                if int(factor) == int(b):
                    value_to_return = f"{int(result)} | {i}"
        except ZeroDivisionError:
            pass
    #Checks the negatives
    for i in range(abs(a_c)):
        i = -i
        try:
            result = a_c/i
            factor = result+i
            if bool((result).is_integer()) != False:
                first,second = f"{a_c} / {i} =  {int(result)}", f"{int(result)} + {i} = {int(factor)}"
                first_length, second_length = " "*(space_length-len(first)), " "*(space_length-len(second))
                #print("|||||", first_length, "|||||", second_length, "|||||")
                print(f"{a_c} / {i} = {int(result)} {first_length} ||| {second_length} {int(result)} + {i} = {int(factor)}")
                if int(factor) == int(b):
                    value_to_return = f"{int(result)} | {i}"
        except ZeroDivisionError:
            pass
    if value_to_return == None:
        print("Cannot be factored. Attempting quadratic formula. . .\n")
        return quadratic_formula(a, b, c)
    return value_to_return

#Quadratic formula
def quadratic_formula(a: int, b: int, c: int):
    top = (other_math.square(b))-(4*a*c)
    bottom = 2*a
    #Shows method of solving
    print(f"(-b±√b^2-4ac)/2a =")
    print(f"(-{b}±√{b}^2-4({a})({c}))/2({a}) =")
    print(f"({-b}±√{other_math.square(b)}-{4*a*c})/{2*a} =")
    print(f"({-b}±√{(other_math.square(b))-(4*a*c)})/{2*a} = ")
    try:
        if bool((math.sqrt(top)).is_integer()) != False:
            value_to_return = f"{Fraction(((-b)-math.sqrt(top))/bottom).limit_denominator()}   or   {Fraction(((-b)+math.sqrt(top))/bottom).limit_denominator()}"
        else:
            value_to_return = f"(-{b}±√{top})/{bottom}"
        return value_to_return
    except ValueError and ZeroDivisionError and ValueError:
        return "Cannot be factored."

print("Loaded!\n")
while True:
    #Asks for a, b, and c
    equation = list(input("Equation: "))
    #Detects breakage
    if "e" in str(equation):
        break
    #Checks if it is a quadratic equation
    count = 0
    for index in equation:
        if index == "x":
            count = count + 1
    if count != 2:
        print("Error: not a quadratic equation. . .\n")
        continue
    #Sorts through equation to find values a, b, and c
    try:
        value_a = int("".join(equation[:equation.index("x")]))
    except ValueError:
        value_a = 1
    try:
        value_b = equation[equation.index("x")+3:]
        value_b = int("".join(value_b[:value_b.index("x")]))
    except ValueError:
        value_b = 1
    try:
        value_c = equation[equation.index("x")+3:]
        value_c = int("".join(value_c[value_c.index("x")+1:]))
    except ValueError:
        value_c = 0
    print(f"A: {value_a}   B: {value_b}   C: {value_c}")
    print("\n")
    time.sleep(0.5)
    print(f"{factor_quadratic(value_a, value_b, value_c)}\n")
print("Program off.")
