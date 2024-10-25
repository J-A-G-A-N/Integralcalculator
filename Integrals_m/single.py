from scipy.integrate import quad
import numpy as np
import re


def Integral(integrand, lower_limit, upper_limit):
    integral = quad(integrand, lower_limit, upper_limit)
    if abs(int(integral[0])) < 10e-40:
        return 0
    else:
        return integral[0]


def Integrand(func, var, lower_limit, upper_limit):
    
    def substitute_variable(expression, var_name, var_value):
        # Define a regular expression pattern to match variables within parentheses
        pattern = re.compile(r'\b' + re.escape(var_name) + r'\b')

        # Substitute the variable with its value
        expression = re.sub(pattern, str(var_value), expression)

        return expression



    input_expression = func
    input_variable_name = var
    input_variable_value = "x"

    func = substitute_variable(input_expression, input_variable_name, input_variable_value)


    lower_limit = eval(lower_limit)
    upper_limit = eval(upper_limit)
    print(func, lower_limit, upper_limit)
    integrand = lambda x: eval(func)
    return Integral(integrand, lower_limit, upper_limit)