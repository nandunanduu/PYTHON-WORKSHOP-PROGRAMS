def palindrome(pal):

    palin=''.join(pal.split()).lower()
    return palin==palin[::-1]

a=input("Enter a string")
if palindrome(a):
   print("it is Palindrome!")
else:
   print("its not a Palindrome.")

print("Program ends.")
