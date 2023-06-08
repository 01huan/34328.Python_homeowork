def turn(string, count):
    List = []
    while (len(string)):
        List.append(string[-count:])
        string = string[:-count]
    return List

def chinese(number):
    unit = ["", "萬", "億", "兆", "京", "垓", "秭", "穰", "溝", "澗", "正", "載", "極"]
    turned = turn(number, 4)
    result = ""
    for i in range(len(turned)):
        add = ""
        for j in range(len(turned[i])):
            if ((turned[i][j] > '0') or (len(add) > 0)):
                add += turned[i][j]
        if len(add) > 0:
            result = add + unit[i] + result
    return result

def english(number):
    unit = ["", " thousand ", " million ", " billion ", " trillion ", " quadrillion ", " quintillion ", " sextillion ", " septillion ", " octillion ", " nonillion ", " decillion ", " undecillion ", " duodecillion ", " tredecillion ", " quattuordecillion ", " quindecillion "]
    turned = turn(number, 3)
    result = ""
    for i in range(len(turned)):
        add = ""
        for j in range(len(turned[i])):
            if ((turned[i][j] > '0') or (len(add) > 0)):
                add += turned[i][j]
        if len(add) > 0:
            result = add + unit[i] + result
    return result

def scientific(number):
    result = power = ""
    left = number[0]
    right = number[1:]
    count = 0
    for i in range(len(right)-1, 0, -1):
        if (right[i] != '0'):
            break
        else:
            right = right[:-1]
            count += 1        
    char = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    for i in str(len(right) + count):
        power += char[int(i)]
    result = left + "." + right + " × " + "10" + power
    return result

def main():
    print(f"  {n}")
    print(f"= {english(n)}")
    print(f"= {chinese(n)}")
    print(f"= {scientific(n)}")

try:
    n = str(int(input("Enter a positive integer: ")))
    if (int(n) > 0):
        main()
    elif (int(n) == 0):
        print(" 0\n= zero\n= 零\n= 0 × 10⁰")
    else:
        print("The number can't be negative.")
except Exception as error:
    print("Error Type: ", error)