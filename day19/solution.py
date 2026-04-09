def safe_divide(a,b):
    try:
        return a/float(b)
    except:
        return ("Cannot divide by zero")


print(safe_divide(5,10))