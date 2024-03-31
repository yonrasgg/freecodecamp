import re


def arithmetic_arranger(problems):
    first = ""
    second = ""
    lines = ""
    sufix = ""
    string = ""
    for problem in problems:
        if (re.search("[^\s0-9.+-]", problem)):
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers cannot be more than four digits."
        
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secod_number = problem.split(" ")[2]
        
        if (len(first_number) >= 5 or len(secod_number) >= 5):
            return "Error: Numbers cannot be more than four digits."

    return arranged_problems