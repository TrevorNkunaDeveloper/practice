def safe_divide(a,b):
    if b == 0:
        return ("Cannot divide by zero")

    return a/float(b)

print(safe_divide(5,0))