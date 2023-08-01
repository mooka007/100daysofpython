# *************************** Pw Generator ****************************** #



import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! ")
pw_letters = int(input("How many letters would you like in your password? : \n")) 
pw_symbols = int(input(f"How many symbols would you like? : \n"))
pw_numbers = int(input(f"How many numbers would you like? : \n"))


pw = []

for char in range(1, pw_letters + 1):
  pw.append(random.choice(letters))

for char in range(1, pw_symbols + 1):
  pw += random.choice(symbols)

for char in range(1, pw_numbers + 1):
  pw += random.choice(numbers)


print(pw)
random.shuffle(pw)
print(pw)

password = ""
for char in pw:
  password += char

print(f"Your password is: {password}")