
# Find the n'th Lucas number
def lucas_number(n):
    if n == 0:
        return 2
    if n == 1:
        return 1;
    
    return lucas_number(n - 1) + lucas_number(n - 2)

