name=''
while not name:
    print('enter name')
    name = input('>')
print('How many guest will you have?')
numberofGuest =int(input('>'))

if numberofGuest:
    print('Be sure to have enough room for all guests.')
print('Done.')