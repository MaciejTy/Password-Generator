#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_generator = ""
for letter in range(nr_letters):
  password_generator += random.choice(letters)

for symbol in range(nr_symbols):
  password_generator += random.choice(symbols)

for number in range(nr_numbers):
  password_generator += random.choice(numbers)

#print(password_generator)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""
tab = []
for letter in range(nr_letters):
  tab.append(random.choice(letters))

for symbol in range(nr_symbols):
  tab.append(random.choice(symbols))

for number in range(nr_numbers):
  tab.append(random.choice(numbers))

random.shuffle(tab)

for n in range(len(tab)):
  password += tab[n]

print(f"Your generated password is: {password}")

