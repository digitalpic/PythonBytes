def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
        '''return statement without\
           a value is equivalent to return None'''


print(maximum(2, 3))
