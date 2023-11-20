a=input("Enter the word")
vow=""
non_vow=""
for x in a:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        vow=vow+x
    else:
        non_vow=non_vow+x

print("Vowels are:",vow,"len",len(vow))
print("Non vowels are:",non_vow,"len",len(non_vow))
print("Program ends")

