number_of_guess=5
key=7
while (True):
    print("Number of guesses left:",number_of_guess, "\n")
    if number_of_guess==0:
        print("Oops! Out of guesses.")
        break
    num=int(input("Enter number:"))
    if num==key:
        print("Congratulations! You got it.")
        print("Number of guesses left:", number_of_guess)
        break
    elif num<key:
        print("Enter greater number.")
        number_of_guess=number_of_guess-1
        continue
    elif num>key:
        print("Enter lesser number.")
        number_of_guess = number_of_guess - 1
        continue