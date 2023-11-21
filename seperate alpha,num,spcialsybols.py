def sprc(string):
 alpha=" "
 num=" "
 sybol=" "
for char in string:
      if char.isaplha():
         alpha+=char
      elif char.isdigit():
         num+=char
      else:
         symbols+=char
         
   return alpha, num,symbols

      
a=input("enter a string")
b=sprc(a)
print("alphabets are:",b[0])
print("numbers are:",b[1])
print("spcial sybols are:",b[2])
