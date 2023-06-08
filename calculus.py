power_char = ["", "x", "x²", "x³", "x⁴", "x⁵", "x⁶", "x⁷", "x⁸", "x⁹"]
coefficients = []
deri_coefficients = []
integ_coefficients = []

def add(highest):
    while (highest):
        coefficient = eval(input(f"Coefficients of the {highest}-th degree: "))
        coefficients.append(coefficient)
        highest -= 1
    coefficients.append(eval(input("Coefficients of the constant degree: ")))
    print()
    for i in range(len(coefficients)):
        if (coefficients[i] == int(coefficients[i])):
            coefficients[i] = int(coefficients[i])

def f():
    print("f(x) = ", end = "")
    print(f"{coefficients[0]}{power_char[len(coefficients)-1]}", end = " ")
    for i in range(1, len(coefficients)):
        if (coefficients[i] > 0):
            print(f"+", end = "")
        elif (coefficients[i] < 0):
            print(f"-", end = "")
        else:
            continue
        print(f" {abs(coefficients[i])}{power_char[len(coefficients) - (i+1)]} ", end = "")

def derivative():
    print("\nf′(x) = ", end = "")
    for i in range(len(coefficients) - 1):
        deri_coefficients.append((coefficients[i]) * (len(coefficients)-i-1))
    print(f"{deri_coefficients[0]}{power_char[len(deri_coefficients)-1]}", end = " ")
    for i in range(1, len(deri_coefficients)):
        if (deri_coefficients[i] > 0):
            print(f"+", end = "")
        elif (deri_coefficients[i] < 0):
            print(f"-", end = "")
        else:
            continue
        print(f" {abs(deri_coefficients[i])}{power_char[len(deri_coefficients) - (i+1)]} ", end = "")
    
def integral():
    print("\n∫ f(x)dx = ", end = "")
    for i in range(len(coefficients)):
        integ_coefficients.append(coefficients[i] / (len(coefficients)-i))
    for i in range(len(integ_coefficients)):
        if (integ_coefficients[i] == int(integ_coefficients[i])):
            integ_coefficients[i] = int(integ_coefficients[i])
    print(f"{integ_coefficients[0]}{power_char[len(integ_coefficients)]}", end = " ")

    for i in range(1, len(integ_coefficients)):
        if (integ_coefficients[i] > 0):
            print(f"+", end = "")
        elif (integ_coefficients[i] < 0):
            print(f"-", end = "")
        else:
            continue
        print(f" {abs(integ_coefficients[i])}{power_char[len(integ_coefficients) - i]} ", end = "")
    print("+ C")

def calculus():
    f()
    derivative()
    integral()

try:
    highest = int(input("The highest power: "))
    if (highest < 0):
        print("(Error)")
    else:
        add(highest)
        if (len(coefficients) > 1):
            calculus()
        else:
            print(f"f(x) = {coefficients[0]}\nf′(x) = 0\n∫ f(x)dx = {coefficients[0]}x + C")
    print()
except Exception as error:
    print("Error:", error)