email=input("enter the email addres")
username=email[:email.index('@')]
service_provider=email[email.index('@'):-4]
domain=email[email.index('.'):]

print("username: ",username)
print("service provider: ",service_provider)
print("domain: ",domain)
