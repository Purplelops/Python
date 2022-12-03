# Find the n'th Lucas number
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1;
    
    return lucas(n - 1) + lucas(n - 2)

def check_number(n):
    # if number is divisble by two, it's not prime
    if user_input % 2 == 0:
        print("number is not prime")
        return
    
    if (lucas(n) - 1) % n == 0:
        print("number is maybe prime")
    else:
        print("number is not prime")

user_input = int(input("Enter a number you want to check: "))

check_number(user_input)