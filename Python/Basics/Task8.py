# Write a program that uses a for loop to iterate through a list of numbers and print each one.
# li = [2,5,7,9,85] this is an easy way to create a list and then reiterate through it but if we want the user to input it then use the below function spplit to create a list
# for num in li:
#     print(num)
lis = input("Enter numbers separated by spaces: ")
num_list = lis.split()
print(num_list)
for num in num_list:
    print(num)
