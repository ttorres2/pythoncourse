#---Define the functions in the game.---
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions: #displays questions
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter  (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#---------------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("You are correct!")
        return 1
    else:
        print("You are incorrect!")
        return 0
#---------------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score =(correct_guesses/len(questions))*100
    print("Your score is: "+str(score)+"%")
#---------------------------------------
def play_again():

    response = input("Do you want to play again? (yes or no):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#---------------------------------------

#create a dictionary to house all the questions:
questions = {
    "Who created Python?: ": "A", #assign the key value pair, which A would be the right answer.
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

#create 2D list (list of lists)
options =   [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

#call the new game function to begin a new game
new_game()

while play_again():
    new_game()

print("Bye.")