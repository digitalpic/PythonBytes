
number = 23
guess = int(input('Enter an integer :'))


if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you don\'t win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it\'s a little higher than that')
else:
    print('No it\'s a little lower than that')

print('Done')
