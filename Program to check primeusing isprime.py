def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


numtocheck=int(input("enter any num"))
if is_prime(numtocheck):
    print(f"{numtocheck}is a prime num")
else:
    print(f"{numtocheck}is not a prime")
