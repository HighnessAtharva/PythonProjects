import random

print("Password Generator")
print("==================")

chars = '~`!@#$%^&*()_-+={[}]|\:;\"\'<,>.?/QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789'
number = int(input("Enter number of passwords to be generated: "))
length = int(input("Password Length?: "))

print("Generated Passwords are:\n========================\n ")
for pwd in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f'Password {pwd+1}: {password}')
