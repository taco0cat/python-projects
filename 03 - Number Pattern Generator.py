def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    pattern_str = ""
    for i in range(1, n+1):
        pattern_str += str(i) + " "
    
    return pattern_str.strip()

print(number_pattern(4))
print(number_pattern(12))
