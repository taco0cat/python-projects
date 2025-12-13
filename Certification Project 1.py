# Build an Arithmetic Formatter Project

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_lines = []
    second_lines = []
    dash_lines = []
    results = []
    
    for problem in problems:
        if "+" in problem:
            operator = "+"
            exp1, exp2 = problem.split("+")
        elif "-" in problem:
            operator = "-"
            exp1, exp2 = problem.split("-")
        else:
            return "Error: Operator must be '+' or '-'."

        exp1 = exp1.strip()
        exp2 = exp2.strip()

        if len(exp1) > 4 or len(exp2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        if not(exp1.isdigit() and exp2.isdigit()):
            return 'Error: Numbers must only contain digits.'


        width = max(len(exp1), len(exp2)) + 2
        formatted_top = exp1.rjust(width)
        formatted_bottom = operator + exp2.rjust(width - 1)
        dashes = "-" * width

        first_lines.append(formatted_top)
        second_lines.append(formatted_bottom)
        dash_lines.append(dashes)

        if show_answers:
            if operator == "+":
                ans = int(exp1) + int(exp2)
            else:
                ans = int(exp1) - int(exp2)
            
            results.append(str(ans).rjust(width))

    first_lines = '    '.join(first_lines)
    second_lines = '    '.join(second_lines)
    dash_lines = '    '.join(dash_lines)

    if show_answers:
        results = '    '.join(results)
        return first_lines + "\n" + second_lines + "\n" + dash_lines + "\n"+results
    else:
        return first_lines + "\n" + second_lines + "\n" + dash_lines

# Final Verification Case
print("Final Verification Case")
print(f'\n{arithmetic_arranger(["32 + 698", "3801 + 2", "45 - 43", "123 - 49"], True)}')

# # All Test Cases
# print("\n\nTest Cases")

# print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
# print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))

# # Error Cases
# print("\n\nError Test Cases")
# print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

# # Result Test Cases
# print("\n\nShow Result Test Cases")
# print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))