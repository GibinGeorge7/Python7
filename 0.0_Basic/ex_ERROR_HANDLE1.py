

def divby(no):
    try:
        return 42/no
    except ZeroDivisionError:
        return ("DIVIDE by ZERO not allowed")

print(divby(1))
print(divby(42))
print(divby(0))
print(divby(22))

