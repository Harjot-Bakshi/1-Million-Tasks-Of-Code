def prime_checker(number):
    if number<=1:
        print("It's not a prime number.")
    for i in range(2,int(number**0.5)+1):
      if number % i == 0:
        print("It's not a prime number.")
        return
    print("It's a prime number.")

n = int(input(f"Please enter a number to check if prime or not prime number:\n")) 
prime_checker(number=n)
