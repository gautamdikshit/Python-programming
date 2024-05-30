# defining functions
import datetime
def getdate():
    return datetime.datetime.now()

def client_function(client_number:int,client_choice:int):
    if client_id==1:
        if client_number == 1:
            print("Press 1 to log diet and 2 to log exercise:")
            log_choice = int(input())
            if log_choice == 1:
                h1 = open("Harry_diet.txt", "a")
                print("Enter diet:")
                diet_var = input()
                h1.write(str(getdate()) + ":\t" + diet_var + "\n")
                h1.close()
                print("Successfully updated.")
            elif log_choice == 2:
                h2 = open("Harry_exercise.txt", "a")
                print("Enter exercise:")
                exercise_var = input()
                h2.write(str(getdate()) + ":\t" + exercise_var + "\n")
                print("Successfully updated.")
                h2.close()
        elif client_number == 2:
            print("Press 1 to view diet and 2 to view exercise log:")
            retrieve_choice = int(input())
            if retrieve_choice == 1:
                f = open("Harry_diet.txt")
                print(f.read())
                f.close()
            elif retrieve_choice == 2:
                f = open("Harry_exercise.txt")
                print(f.read())
                f.close()
    elif client_id==2:
        if client_number == 1:
            print("Press 1 to log diet and 2 to log exercise:")
            log_choice = int(input())
            if log_choice == 1:
                h1 = open("Rohan_diet.txt", "a")
                print("Enter diet:")
                diet_var = input()
                h1.write(str(getdate()) + ":\t" + diet_var + "\n")
                h1.close()
                print("Successfully updated.")
            elif log_choice == 2:
                h2 = open("Rohan_exercise.txt", "a")
                print("Enter exercise:")
                exercise_var = input()
                h2.write(str(getdate()) + ":\t" + exercise_var + "\n")
                print("Successfully updated.")
                h2.close()
        elif client_number == 2:
            print("Press 1 to view diet and 2 to view exercise log:")
            retrieve_choice = int(input())
            if retrieve_choice == 1:
                f = open("Rohan_diet.txt")
                print(f.read())
                f.close()
            elif retrieve_choice == 2:
                f = open("Rohan_exercise.txt")
                print(f.read())
                f.close()
    elif client_id==3:
        if client_number == 1:
            print("Press 1 to log diet and 2 to log exercise:")
            log_choice = int(input())
            if log_choice == 1:
                h1 = open("Hammad_diet.txt", "a")
                print("Enter diet:")
                diet_var = input()
                h1.write(str(getdate()) + ":\t" + diet_var + "\n")
                h1.close()
                print("Successfully updated.")
            elif log_choice == 2:
                h2 = open("Hammad_exercise.txt", "a")
                print("Enter exercise:")
                exercise_var = input()
                h2.write(str(getdate()) + ":\t" + exercise_var + "\n")
                print("Successfully updated.")
                h2.close()
        elif client_number == 2:
            print("Press 1 to view diet and 2 to view exercise log:")
            retrieve_choice = int(input())
            if retrieve_choice == 1:
                f = open("Hammad_diet.txt")
                print(f.read())
                f.close()
            elif retrieve_choice == 2:
                f = open("Hammad_exercise.txt")
                print(f.read())
                f.close()
# Main Program
print("Enter 1 to log and 2 to retrieve:")
var_action=int(input())
print("Clients:")
print("Press '1' for Harry.")
print("Press '2' for Rohan.")
print("Press '3' for Hammad.")
print("\nPick your client:")
client_id=int(input())
if var_action==1:
    client_function(var_action,client_id)
elif var_action==2:
    client_function(var_action,client_id)