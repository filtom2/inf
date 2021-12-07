import random
import re

slovnik_slov = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()



random_choice = random.choice(slovnik_slov)

number_of_tries_full = len(list(random_choice)) - 1
number_of_tries = len(list(random_choice)) - 1


tries = f'{number_of_tries} / {number_of_tries_full} lives '
print(tries)

guessed_word = []

for i in range(len(random_choice)):
    guessed_word.append('_')

print(guessed_word)

while number_of_tries >= 0:
    guess = input('\nWrite either a letter or a full answer if u think u got this: ')
    tries = f'{number_of_tries} / {number_of_tries_full} lives '

    if len(guess) == 1:
        if guess in list(random_choice):

            index_of_the_guess = [n for (n, e) in enumerate(random_choice) if e == f'{guess}']

            for j in range(len(index_of_the_guess)):
                guessed_word[index_of_the_guess[j]] = f'{guess}'

            print(guessed_word)

            continue



        else:
            print('nespravne uhadnute pismeno')
            number_of_tries -= 1
            print(tries)
            continue


    else:
        if guess == random_choice:
            print('\nYou guessed correctly congratz. ')
            break

        else:
            print('Wrong choice try again. If u have the lives to spare. ')
            number_of_tries -= 1
            print(tries)
            continue

print('\nggwp')
