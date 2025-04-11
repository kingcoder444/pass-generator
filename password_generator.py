import random
import string

length = int(input("Enter password length: "))
all_chars = string.ascii_letters + string.digits + string.punctuation

password = []
password.append(random.choice(string.ascii_uppercase))

for i in range(length - 1):
    password.append(random.choice(all_chars))

random.shuffle(password)
final_password = ''.join(password)

print("Generated Password:", final_password)
