# this is program of guessing a random number game
import random
print("WELCOME TO THE GAME!!\nRULES-\n1.Guess the number between 1 and 100\n2.please select only number not a charecter or alphabatical word\n")
while True:
    attempt = 0
    #genrate no between 1 to 100
    random_no = random.randint(1,100)
    print("NUMBER IS GENRATED.")


    while True:
        try:
            user_no = int(input("enter the number. \n"))
            attempt+=1
            if(random_no == user_no):
                print(f"CONGRATS! Your No is correct.\nYou take {attempt} attempts.")
                break
            elif(random_no < user_no):
                print("TOO HIGH.")
            elif(random_no > user_no):
                print("TOO LOW.")
        except ValueError:
            print("invalid!! please enter numeric value.")

    
    choice = input("Do you want to play it again(yes/no)?").lower()
    if choice == 'no':
        print("thanks for playing.")
        break


