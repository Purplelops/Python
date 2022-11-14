import math

# Ask the user for input and convert it to an int
num = int(input("Input the number you want to check: "))

# Check if number is divisible by two
if num % 2 == 0:
    print("Number is not prime! It is divisible by 2")
    exit()

divisor = 3

# Loop over all numbers less than half of the number the user picked
while True:
    # If the number's remainder is zero, then it's not prime
    if num % divisor == 0:
        print("Number is not prime! It is divisible by", divisor)
        break;
    else:
        # Check if the number is still less than half of the input number
        if divisor == math.floor(num / 2):
            print("Number is prime!")
            break;
        else:
            # Add two to the divisor and repeat
            # I add two, because any number divisible by an even number must be even
            divisor += 2
