num=int(input("enter the fabbonocci series"))
a=1
b=1
fibonacci_series=[]
for num in range(num):
    fibonacci_series.append(a)
    a,b=b,a+b
print("fibanacci series:")
for term in fibonacci_series:
    print(term,end=",")
