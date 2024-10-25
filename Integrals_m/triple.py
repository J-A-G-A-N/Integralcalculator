import re
from scipy.integrate import tplquad
import numpy as np


def Integral(integrand, inner_ll_1, inner_ul_1, inner_ll_2, inner_ul_2, outer_ll, outer_ul):
    try:
        result, _ = tplquad(integrand, inner_ll_1, inner_ul_1,inner_ll_2,inner_ul_2, outer_ll, outer_ul)  # type: ignore
        return result
    except Exception as e:
        print(f"Integration error: {e}")
        return 0


def Integrand(func, var_1, var_2, var_3 , inner_ll_1, inner_ul_1 , inner_ll_2, inner_ul_2,  outer_ll, outer_ul):
    def substitute_variables(func, substitutions):
        for var_name, var_value in substitutions.items():
            pattern = re.compile(r"\b" + re.escape(var_name) + r"\b")
            func = re.sub(pattern, str(var_value), func)
        return func

    substitutions = {var_1: "x", var_2: "y" , var_3 : "z"}
    func = substitute_variables(func, substitutions)

    integrand = lambda x, y , z : eval(func)

    inner_ll_1 = eval(inner_ll_1)
    inner_ul_1 = eval(inner_ul_1)
    inner_ll_2 = eval(inner_ll_2)
    inner_ul_2 = eval(inner_ul_2)
    outer_ll = eval(outer_ll)
    outer_ul = eval(outer_ul)

    return Integral(integrand, inner_ll_1, inner_ul_1, inner_ll_2, inner_ul_2, outer_ll, outer_ul)