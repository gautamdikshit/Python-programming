import random

options=["rock","paper","scissor"]
user_win_count=0
computer_win_count=0

while True:
    user_input = input("Choose rock/paper/scissor or q to quit. ").lower()
    if user_input == "q":
        print("Thank you!")
        quit()
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    #rock:0, paper:1, scissor:2

    computer_pick=options[random_number]
    print("Computer pick:",computer_pick)

    if user_input=='rock'and computer_pick=='scissor':
        print("You win!")
        user_win_count+=1
    elif user_input=='paper' and computer_pick=='rock':
        print("You win!")
        user_win_count+=1
    elif user_input=='scissor' and computer_pick=='paper':
        print("You win!")
        user_win_count+=1
    else:
        print("Computer wins!")
        computer_win_count+=1
    print("User wins:", user_win_count)
    print("Computer wins:", computer_win_count)
    print("\n")

