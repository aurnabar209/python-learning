import random

secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 to 20: ")

#Ask 6 times 
for gueses_taken in range(1, 7):
    print('Take a guess: ')
    gueses_taken =int(input('>'))

    if gueses_taken< secret_number:
        print('The guess is too low!!')

    elif gueses_taken> secret_number:
        print('The guess is too high!!')
    else:sortedSunjeeda 
        break
    
if gueses_taken == secret_number:
        print('Good!Job! you got it in', gueses_taken, 'guesses!')
else:
     print('nope. the guess was ', secret_number)