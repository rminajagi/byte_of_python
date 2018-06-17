number=23
running = True
while running:
    guess = int(raw_input("enter an integer:"))

    if guess == number:
        print'congrats,you got it.'
        running = False

    elif guess < number:
        print'no,it is higher than that.'
    else:
        print'it is lower than that.'

else:
    print'the while loop is over.'

print 'Done'