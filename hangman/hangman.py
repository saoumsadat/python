import random
from words import word_list

user_choices = []   #user choices will be added to the list
guessed = False    #it will turn true if guessed correctly

#choosing a word
chosen_word = random.choice(word_list)

#getting number of tries from the user
num_tries = int(input("Enter number of tries: "))

#uncomment this line to see the word
print(chosen_word)

for x in range(0, num_tries):
    displayed_word = ""

    #uncomment this line to see choices
    # print(user_choices)

    #generating display word
    for char in range(0, len(chosen_word)):
        if chosen_word[char] in user_choices:
            displayed_word += displayed_word.join(chosen_word[char])   #adding the letter if it is in the choices
        else:
            displayed_word += displayed_word.join("_")  #otherwise adding "_"
    
    print(displayed_word)

    #if chosen correcty, it will turn true, otherwise it will remain false
    if displayed_word == chosen_word:
        guessed = True
        break

    user_choices.append(input("your choice:"))  #getting a choice and add to the list

    print("Tries left: %d" % ((num_tries - x) - 1))    #displaying how many tries are left


if guessed:
    print("Congratualtions! You have successfully guessed the word")
else:
    print("Sorry! you have failed to guess the word. It was '%s'" % chosen_word)