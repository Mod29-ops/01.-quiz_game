# Intro
print("wlcome to my quiz game!")

# ask permission to user for playing quiz
check = input("do you want to play this game? \n").lower()
if check != 'yes':
    quit()

marks = 0 # initialize mark variable as 0

# list of dictionaries where we store our que and ans .
question =[{"q": "1. What is the capital of France?", "a": "paris"},
    {"q": "2. Which planet is known as the Red Planet?", "a": "mars"},
    {"q": "3. What is the largest mammal on Earth?", "a": "blue whale"},
    {"q": "4. Which gas do humans inhale to survive?", "a": "oxygen"},
    {"q": "5. What is the fastest land animal?", "a": "cheetah"}]

# loop for print question and check it
for item in question:
    answer = input(item['q'] + "\n").lower() # use lower case to prevent from case sensitive errors
    # check the answer
    if answer == item['a']:
        print("you are correct.")
        marks+=1
    else:
        print("you are wrong the correct answer is " + item["a"])

# print finale result
print(f"you got {marks}/5 marks")
print(f"you have total score of {(marks/5)*100}%")
