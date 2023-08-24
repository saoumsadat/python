import random;

# print welcome msg
print("Welcome to rock, paper and scissors!\n");

# global variable choices
choices = ["rock", "paper", "scissors"];


def take_user_choice(choices):

    # keep taking input until valid choice is provided
    while (True):
        user_choice = input("Enter your choice:\n1. rock\n2. paper\n3. scissors\n\n");

        # checking validity
        if user_choice in choices: 
            return user_choice;
        elif user_choice in ["1", "2", "3"]:
            return choices[int(user_choice) - 1];
        else:
            print("Enter valid choice plz\n");

def take_computer_choice(choices):
    return random.choice(choices);

def compare_choices(choice_list):
    
    if choice_list["user"] == choice_list["computer"]:
        return "Tie"

    elif choice_list["user"] == "rock" and choice_list["computer"] == "paper":
        return "You lose!"
    elif choice_list["user"] == "rock" and choice_list["computer"] == "scissors":
        return "You win!"
    elif choice_list["user"] == "paper" and choice_list["computer"] == "scissors":
        return "You lose!"
    elif choice_list["user"] == "paper" and choice_list["computer"] == "rock":
        return "You win!"
    elif choice_list["user"] == "scissors" and choice_list["computer"] == "rock":
        return "You lose!"
    elif choice_list["user"] == "scissors" and choice_list["computer"] == "paper":
        return "You win!"
    
def print_result(choice_list, result):
    print(f"Your choice: {choice_list['user']}");
    print(f"Computer's choice: {choice_list['computer']}");
    print(result);


def check_restart():

    # keep asking until valid input is provided
    while (True):
        restart = input("Play Again? (Yes/No) : ");
        
        if restart == "yes":
            return True;
        elif restart == "no":
            return False;



# keep playing till user decides to terminates
while (True):

    # generate object with both choices
    choice_list = {
        "user" : take_user_choice(choices),
        "computer" : take_computer_choice(choices)
    }

    # get result
    result = compare_choices(choice_list);

    # print result
    print_result(choice_list, result);

    want_restart = check_restart();

    if want_restart:
        continue;
    else:
        break;

print("Goodbye!");
