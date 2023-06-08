def BIN(n):
    list2 = []
    char = [0, 1]   
    while (1):
        list2.append(n % 2)
        n //= 2
        if (n < 2):
            list2.append(n)
            break
    for i in range(len(list2)):
        list2[i] = char[list2[i]]
    list2 = list2[(len(list2) - 1) ::-1] 
    for i in list2:
        print(i, end = "")

def HEX(n):
    list16 = []
    char = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]   
    while (1):
        list16.append(n % 16)
        n //= 16
        if (n < 16):
            list16.append(n)
            break
    for i in range(len(list16)):
        list16[i] = char[list16[i]]
    list16 = list16[(len(list16) - 1) ::-1]
    for i in list16:
        print(i, end = "")

def OCT(n):
    list8 = []
    char = [0, 1, 2, 3, 4, 5, 6, 7]   
    while (1):
        list8.append(n % 8)
        n //= 8
        if (n < 8):
            list8.append(n)
            break
    for i in range(len(list8)):
        list8[i] = char[list8[i]]
    list8 = list8[(len(list8) - 1) ::-1]
    for i in list8:
        print(i, end = "")

n = int(input("Enter a decimal number: "))

print("%d_(10) = " %(n), end = "")
BIN(n)
print("_(2) = ", end = "")
OCT(n)
print("_(8) = ", end = "")
HEX(n)
print("_(16)\n")