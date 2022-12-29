email = input("enter your email")

index = email.index("@")

username = email[0:index]
domain = email[index+1:]
print(username)
print(domain)
