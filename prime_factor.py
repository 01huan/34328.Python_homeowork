def superscript(n):
    char = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    str_n = str((n))
    result = ""
    for i in str_n:
        result += char[int(i)]
    return result 

def factor(n):
    List = []
    for i in range(1, n+1):
        if (n % i == 0):
            List.append(i)
    return List

def isPrime(n):
    divisor = 2
    if (n > 1):
        flag = True
    else:
        flag = False
    while ((divisor < n) and (flag)):
        if (n % divisor == 0):
            flag = False
            break
        divisor += 1
    return flag

def primeFactor(n):
    List = []
    for i in factor(n):
        if (isPrime(i)):
            List.append(i)
    return List

try:
    num = int(input("Enter a positive integer: "))
    if (num >= 2):
        number = num
        power = []
        for i in range(len(primeFactor(number))):
            power.append(0)

        PrimeFactors = primeFactor(number)
        for i in range(len(PrimeFactors)):
            Factor = PrimeFactors[i]
            while (number % Factor == 0):
                number //= Factor
                power[i] += 1

        print(f"{num} = ", end = "")
        for i in range(len(power)):
            print(PrimeFactors[i], end = "")
            if (power[i] == 1):
                print("", end = "")
            else:
                print(superscript(power[i]), end = "")
            if (i == len(power)-1):
                print()
            else:
                print(" × ", end = "")
    else:
        print(num, "=", num)
except Exception as error:
    print("Error:", error)