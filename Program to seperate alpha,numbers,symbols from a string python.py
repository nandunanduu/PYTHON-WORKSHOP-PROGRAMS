def seperate_char(string):
    alphabets=""
    numbers=""
    symbols=""

    for ch in string:
        if ch.isalpha():
           alphabets+=ch
        elif ch.isdigit():
           numbers+=ch
        else:
            symbols+=ch

    return alphabets, numbers, symbols

a=input("enter a string")
b=seperate_char(a)
print("alphabets are:",b[0])
print("numbers are:",b[1])
print("special symbols are:",b[2])
