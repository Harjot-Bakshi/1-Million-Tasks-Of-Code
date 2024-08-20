# Random Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_l= int(input("How many letters would you like in your password?\n"))
nr_s = int(input(f"How many symbols would you like?\n"))
nr_n = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
max_index = len(letters)-1
indices_letters = [random.randint(0,max_index) for x in range(nr_l)]
combined_letter = [letters[index] for index in indices_letters]
max_index_numbers = len(numbers)-1
indices_numbers = [random.randint(0,max_index_numbers) for x1 in range(nr_n)]
combined_number = [numbers[index1] for index1 in indices_numbers]
max_index_symbols = len(symbols)-1
indices_symbols = [random.randint(0,max_index_symbols) for x2 in range(nr_s)]
combined_symbol = [symbols[index2] for index2 in indices_symbols]
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = combined_letter+combined_number+combined_symbol
random.shuffle(random_password)
password = ''.join(random_password)
print(password)
