# Project: Code Your Own Quiz
import time

Hard = '''Generally speaking, methods of temporal measurement, or __1__, take two distinct forms: 
the __2__, a mathematical tool for organising intervals of time, and the __3__, a physical mechanism 
that counts the passage of __4__. In day-to-day life, the __3__ is consulted for periods less than 
a day whereas the __2__ is consulted for periods longer than a day.'''

Normal = '''A __1__ (or automobile) is a wheeled __2__ vehicle used for __3__. 
Most definitions of __1__ say they run primarily on roads, seat one to eight people, 
have four __4__, and mainly transport people rather than goods.'''

Easy = '''The __1__ (Panthera leo) is one of the big __2__ in the genus Panthera and a member of 
the family Felidae. __3__ are unusually social compared to other __2__. Highly distinctive, 
the male __1__ is easily recognised by its  __4__.'''

# Fill in the blanks answers
AnswerHard = ["chronometry", "calendar", "clock", "time"]
AnswerNormal = ["car", "motor", "transportation", "tires"]
AnswerEasy = ["lion", "cats", "Lions", "mane"]

'''Difficult selection for game.
Input difficulty based on user input
output difficulty by full name (Easy, Normal, Hard)'''
def Difficulty(difficulty):
    difficulty = difficulty.upper()
    if difficulty == "E":
        difficulty = "Easy"

    if difficulty == "N":
        difficulty = "Normal"

    if difficulty == "H":
        difficulty = "Hard"
    return difficulty

''' User answer check for correct input user_answer, true answers and answers index, record and record index
 output if 3 times making  mistake program ends and make end statement or if answer correct turns correct answer statement'''
def AnswerValidation (user_answer, answers, index_answer, index_record, record):
    fault_count = 0
    if user_answer.lower() != answers[index_answer].lower():
        fault_count = 0
        while user_answer.lower() != answers[index_answer].lower():
            fault_count += 1
            if fault_count == 3:
                print (span_length * "|" + "\n" "It's your " + str (fault_count) + " mistake, sorry you lose, play again\n" + span_length * "|")
                exit ()
            user_answer = input ("Your answer is incorrect, it's your " + str (fault_count) + " mistake, try again " +
                                 record[index_record] + ": ")
        return (print ("-" * span_length1 + "\nWell Done! Your answer is correct!\n" + "-" * span_length1))
    else:
        return print ("-" * span_length1 + "\nWell Done! Your answer is correct!\n" + "-" * span_length1)


''' Text and text true answer selection based on user difficulty selection.
 Input difficulty based on user, output a list included true answers and text '''
def AnswerSellect(difficulty):
    text = ""
    answers = []
    select = Difficulty(difficulty)
    if select == "Easy":
        text = Easy
        answers = AnswerEasy
    if select == "Normal":
        answers = AnswerNormal
        text = Normal
    if select == "Hard":
        answers = AnswerHard
        text = Hard
    return [answers, text]


'''main game code. Input difficulty which is based on user and record list.
 Output success text. '''
def Fill_Blanks(difficulty, record):
    index_record, index_answer = 0, 0
    answers = AnswerSellect(difficulty)[0]
    text = AnswerSellect(difficulty)[1]
    time.sleep(3)
    print("="*span_length + "\n" + text + "\n" + "="*span_length )
    time.sleep(2)
    while index_record < len(record):
        while index_answer < len(answers):
            user_answer = input (" Fill in the blanks as a appropriate word " + record[index_record] + ": ")
            AnswerValidation (user_answer, answers, index_answer, index_record, record)
            text = text.replace(record[index_record], answers[index_answer])
            time.sleep(2)
            print ("=" * span_length1 + "\n" + text + "\n" + "=" * span_length1)
            index_record += 1
            index_answer += 1
    return print("*" * span_length1 +"\nNice Job!, you finish quiz " + Difficulty(difficulty) + " part.\n" + "*" * span_length1 )

'''Game played on this function.
Input none. Output the main code, function Fill_Blanks'''
def Play_Game():
# represents the quiz blanks
    record = ["__1__", "__2__", "__3__", "__4__"]
    print("*" * span_length1 + "\n    !!!Welcome to Fill in the Blanks Game!!!\n" + "*" * span_length1)
    time.sleep(3)
    difficulty =  input("Select the game difficulty ( E for Easy, N for Normal, and H for Hard (Press E, N or H): ")
    while difficulty.upper() != "E" and difficulty.upper() != "N" and difficulty.upper() != "H":
        difficulty = input ("Select the game difficulty (Press 'E' for Easy, 'N' for Normal, and 'H' for Hard): ")
    print("-"*span_length1 + "\nYou sellect " + Difficulty(difficulty) + " part of the game\n" + "-"*span_length1)
    time.sleep(2)
    print("You have 3 mistakes in each blank to predict the correct word.")
    time.sleep(2)
    print("Fill in the blanks the text below")
    return Fill_Blanks(difficulty,record)

span_length = 100    # numbers should be a magic number so that defines number in a variable
span_length1 = 50


if __name__ == "__main__":
    Play_Game()
