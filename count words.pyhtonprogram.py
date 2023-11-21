def count_words(stri):
    count=stri.split()
    return len(count)

a=input("enter a string")
b=count_words(a)
print("count of string :",b)
