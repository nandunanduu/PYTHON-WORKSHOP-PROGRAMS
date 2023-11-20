def generate_primes(n):
   primes=[]
   for num in range(2,n+1):
      isprime=True
      for i in range(2,int(num**0.5)+1):
          if num%i==0:
             isprime=False
             break
      if isprime:
        primes.append(num)
   return primes

a=int(input("enter the range"))
b=generate_primes(a)
print(b)
