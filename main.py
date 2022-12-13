#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator:\n")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
pass_letters = ""
pass_numbs = ""
pass_symb = ""

# Grabs randomized letters from the letters list and stores them in
# pass_letters variable
for numb in range(0,nr_letters):
  pass_letters += letters[random.randrange(0, len(letters)-1)]

# Grabs randomized numbers from the numbers list and stores them in
# pass_numbs variable
for numb in range(0, nr_symbols):
  pass_numbs += numbers[random.randrange(0, len(numbers)-1)]

# Grabs randomized symbols from the symbols list and stores them in
# pass_symb variable
for numb in range(0, nr_numbers):
  pass_symb += symbols[random.randrange(0, len(symbols)-1)]

# Combines pass_symb, pass_numbs, and pass_letters, randomizes characters and
# stores in string
password_temp = pass_letters+pass_numbs+pass_symb
password_list = list(password_temp)
random.shuffle(password_list)
password = "".join(password_list)

print(f"Your randomized password is: \n{password}. ")

