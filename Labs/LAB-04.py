#LAB-04 - Build a Number Pattern Generator
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        resultado = ''
        for i in range(1,n+1):
            if i == n:
                resultado += str(i)
            else:
                resultado += str(i) + " "
        return f"{resultado}"

# Main Test
print(number_pattern(12))
