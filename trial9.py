def values(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        print(a * b * c)

    else:
        print("Enter Integers or float values")


a = float(input("enter the first Number"))
b = float(input("enter the Second Number"))
c = float(input("enter the first Number"))

values(a,b,c)
