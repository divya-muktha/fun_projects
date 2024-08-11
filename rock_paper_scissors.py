import random
choices = ["rock", "scissor", "paper"]
user_choice = input("Rock Paper Scissor").lower()
computer_choice = choices[random.randint(0, 2)]
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")
user_choice_index = choices.index(user_choice)
computer_choice_index = choices.index(computer_choice)
difference = user_choice_index - computer_choice_index

if difference < 2:
    if choices.index(user_choice) < choices.index(computer_choice):
        print("You win")
    elif choices.index(user_choice) > choices.index(computer_choice):
        print("Computer wins")
    else:
        print("Its a tie")
else:
    if choices.index(user_choice) < choices.index(computer_choice):
        print("Computer wins")
    elif choices.index(user_choice) > choices.index(computer_choice):
        print("You win")
