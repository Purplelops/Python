import math

# Ask the user for input and convert it to an int
num = int(input("Input the number you want to check: "))

divisor = 2

# Loop over all numbers less than half of the number the user picked
while True:
    # If the number's remainder is zero, then it's not prime
    if num % divisor == 0:
        print("Number is not prime!")
        break;
    else:
        # Check if the number is still less than half of the input number
        if divisor == math.floor(num / 2):
            print("Number is prime!")
            break;
        else:
            # Add one to the divisor and repeat
            divisor += 1
    