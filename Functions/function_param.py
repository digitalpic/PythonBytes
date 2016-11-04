def print_max(a, b):  # using two parameters
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equalto', b)
    else:
        print(b, 'is maximum')

# directly pass literal values
print_max(3, 4)


x = 5
y = 7

# pass values as arguments
print_max(x, y)
