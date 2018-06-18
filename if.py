number = 23
guess=int(raw_input('enter an integer :'))
if guess==number:
    print'congrats you got it'
    print'(but u did not win any prize.)'
elif guess<number:
    print"number is little higher than that"
else:
    print"no,it is lower than that"
print 'done'