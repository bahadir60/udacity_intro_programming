from sys import exit
import random
import MathQuiz
import time
import sqlite3

'''Number guess game : The user predicts the number(s) based on the game level. Input difficulty select by user, output guess number(s) list'''
def Number_Guess(difficulty):
    number_user = []
    if difficulty == "Easy":
        '''get user first number'''
        number = input (user_name + " select a number 1 or 2: ")
        number = int (number)
        if number < 0 or number > 2:
            number = input (user_name + " write your number exactly 1 or 2: ")
            number = int (number)
        number_user.append (number)

    if difficulty == "Normal":
        '''get user first number'''
        number1 = input (user_name + " write your first number 1,2 or 3 : ")
        number1 = int (number1)
        if number1 < 0 or number1 > 3:
            number1 = input (user_name + " write your first number exactly 1,2 or 3: ")
            number1 = int (number1)

        '''get user second number not equal first'''
        number2 = input (user_name + " write your second number 1,2 or 3 and different than first number: ")
        number2 = int (number2)
        if number1 == number2 and (number2 < 0 or number2 > 3):
            number2 = input (user_name + " write your second number exactly 1,2 or 3 and different than first: ")
            number2 = int (number2)
        number_user.append (number1)
        number_user.append (number2)

    if difficulty == "Hard":
        number1 = input (user_name + " write your first number 1,2,3 or 4: ")
        number1 = int (number1)
        if number1 < 0 or number1 > 4:
            number1 = input (user_name + " write your first number exactly 1 to 4: ")
            number1 = int (number1)
        '''get user second number not equal first'''
        number2 = input (user_name + " write your second number 1 to 4 and different than first number: ")
        number2 = int (number2)
        if number1 == number2 and (number2 < 0 or number2 > 4):
            number2 = input (user_name + " write your second number exactly 1 to 4 and different than first: ")
            number2 = int (number2)

        '''get user thirth number not equal first or second'''
        number3 = input (user_name + " write your thirth number 1 to 4 and different than first and second: ")
        number3 = int (number3)
        if ((number1 == number3) or (number2 == number3)) and (number3 < 0 or number3 > 4):
            number3 = input (
                user_name + " write your thirth number exactly 1 to 4 and different than first and second: ")
            number3 = int (number3)
        number_user.append (number1)
        number_user.append (number2)
        number_user.append (number3)
    return number_user

'''if user lose, make game over'''
def End():
    print ("Game is Over")
    exit ()

'''Number guess game : Computer randomly make a number(s) list based on the game level. Input num meet to difficulty game level which is select by user, output computer number(s) list'''
def Number_Computer(num):
    number_comp = []
    values = list (range (num + 2))
    # print(values)
    i = 0
    while i < num:
        number = random.choice (values)
        # print(number)
        if number != 0 and number not in number_comp:
            number_comp.append (number)

        elif number == 0:
            while number == 0:
                number = random.choice (values)
                if number in number_comp:
                    while number in number_comp:
                        number = random.choice (values)
            number_comp.append (number)

        elif number in number_comp:
            while number in number_comp:
                number = random.choice (values)
                if number == 0:
                    while number == 0:
                        number = random.choice (values)

            number_comp.append (number)
        i += 1
    return number_comp

'''Flip Coin Game: Randomly choose head or tail'''
def Flip_Coin_Comp():
    flip = ["H", "T"]
    flip_comp = random.choice (flip)
    return flip_comp

'''Throw Dice Game: randomly select dice(s) based on game level. Input game level, output dice(s) list '''
def Dice_Comp(difficulty):
    if difficulty == "Easy":
        dice_comp = random.randint (1, 6)
        if dice_comp > 4:
            dice_comp = random.randint (1, 6)
        return dice_comp

    if difficulty == "Normal" or difficulty == "Hard":
        dicex = False
        dice_comp = []
        while dicex == False:
            dice = []
            dice1 = 0
            dice2 = 0
            dice1 = random.randint (1, 6)
            dice2 = random.randint (1, 6)
            dice.append (dice1)
            dice.append (dice2)
            dice_comp.append (dice)
            if len (dice_comp) > 20:
                dicex = True
        return dice_comp

welcome = "!!! Welcome to Guess Game !!!"
print (welcome + "\n" + len (welcome) * "_")
user_name = input ("Please Write Your Name: ")
user_name = str(user_name).capitalize ()
user_age = input (user_name + " please Write Your Age: ")
while user_age.isnumeric() == False:
    user_age = input (user_name + " please Write Your Age Again: ")
if int (user_age) < 10:
    print (user_name + " the game is not suitable for your age. Good luck. ")
elif int (user_age) < 15:
    print (user_name + "the game is may be not suitable for your age. But, I think you will succeed. ")
else: print (user_name + " the game is suitable for your age. Have fun!!!")
time.sleep(2)
print (" \n" + "*" * 100)
print (user_name + " Guess Game is 4 level. At the beginning of each level, success criteria will be given.\n" + "=" * 100 + "\n" "First game is Number Guess\nSecond game is Flip Coin(Heads or Tails)\nThirth one is Throwing the Dice\n"        "Forth one is MathGame\n" + "=" * 100 + "\nGuess Game is increasingly getting difficult. Do your best!!!")
print ("*" * 100 + " \n" + " ")

'''Game Hardness'''
time.sleep(5)
difficulty = input (user_name + " please select game difficulty(Pls press 1, 2 or 3)\n" + "_" * 30 + "\n" + "1. Easy\n2. Normal\n3. Hard\nYour choose :  ")
while difficulty != "1" and difficulty != "2" and difficulty != "3":
    input (user_name + "'s choose is not valid. Press 1, 2 or 3 for select difficulty of game: ")
if difficulty == "1":
    difficulty = "Easy"
elif difficulty == "2":
    difficulty = "Normal"
else:
    difficulty = "Hard"

# Game-1 Number Guess
num = 1
if difficulty == "Normal":
    num = 2
if difficulty == "Hard":
    num = 3
print (user_name + " welcome to Number Guess Game " + difficulty + " part.\n" + '-' * 100 + "\nThe game is simple. You should guess " + str (num) + " number(s). If they are equal to random computer numbers, you win the game. Let's play, guess a number\n" + "_" * 100)

time.sleep(4)

win = 0
points = 0
mistake = 0
check = False

while win < 3:
    number_comp = Number_Computer (num)
    #print (number_comp)  ##for test don't open when playing
    number_user = Number_Guess (difficulty)

    if num == 1:
        if number_user[0] in number_comp:
            check = True
    elif num == 2:
        if (number_user[0] in number_comp) and (number_user[1] in number_comp):
            check = True
    elif num == 3:
        if (number_user[0] in number_comp) and (number_user[1] in number_comp) and (number_user[2] in number_comp):
            check = True

    print ("Computer Numbers  : " + str (number_comp))
    print (user_name + " Numbers: " + str (number_user))

    if check == True:
        win += 1
        points = points + 100
        print (user_name + "'s Score : " + str (points) + ". Make " + str (300 - points) + " without " + str (3 - mistake) + " mistakes to win\n" + "-"*100)

        if win == 3:
            if num == 1:
                print ("*" * 50 + "\n!!! " + user_name +  " Win !!!\n Your score is 300!!!\n" + "*" * 50)
                score = 300

            if num == 2:
                score = 400
                print ("*" * 50 + "\n!!! " + user_name +  " Win !!!\nYou score is 300 and 100 for hardness of game. Total 400!!!   \n" + "*" * 50)

            if num == 3:
                score = 500
                print ("*" * 50 + "\n!!! " + user_name +  " Win !!!\nYou score is 300 and 200 for hardness of game. Total 500!!!\n" + "*" * 50)

    else:
        mistake += 1
        print ("It's your " + str (mistake) + " mistake.")
        if mistake == 3:
            print ("Sorry" + user_name + " lose. You make 3 mistake.")
            # replay code comes here
            End()


time.sleep(3)
# Game-2 Flip Coin
print (user_name + " welcome to FLIP THE COIN GAME (HEADS or TAILS) " + difficulty + " part.")
time.sleep(2)
print('-' * 100 + "\nThe game is simple. Your score is your money. Make a bid, than bet your money and flip a coin, win or lose.\nif your money downs 0 you lose, if your money increases by 5 times you win.\nLet's play, make a bid and flip the coin, guess HEAD or TAIL\n" + "-" * 100)
time.sleep(4)

bet_money = 0
flip_coin = " "
money = score
win_money = money * 5

while money < win_money:

    while True:
        try:
            bet_money_str = input (user_name + "'s money is $" + str (money) + ". Make a bid :  ")
            bet_money = int (bet_money_str)
            break
        except ValueError:
            bet_money_str = input ("Please write only numeric. Your money is $" + str (money) + ". Make a bid :  ")

    while bet_money > money or bet_money < 0:
        bet_money_str = input ("You have exceeded the amount bet, your money is now $" + str (money) + ". Make a bid:  ")
        bet_money = int (bet_money_str)

    flip_comp = Flip_Coin_Comp ()
    #print (flip_comp)  ##for test don't open when playing
    flip_coin = input ("HEADS or TAILS, H or T: ")
    time.sleep(1)

    if flip_coin.upper () != "T" and flip_coin.upper () != "H":
        while flip_coin.upper () != "T" and flip_coin.upper () != "H":
            flip_coin = input ("Please press H for HEADS or T for TAILS, H or T: ")

    if flip_comp == flip_coin.upper ():
        money = money + bet_money
        time.sleep(1)
        print ("Nice Job " + user_name + ". You won $" + str (bet_money) + ". " + user_name + "'s total money is: " + str(money) + "\n" + "-"*100)
        if money >= win_money:
            print ("*" * 50 + "\"\n!!! " + user_name +  " Win !!!\n"  + user_name + "'s total money is $" + str (money) + "\n" + "*" * 50)

    else:
        money = money - bet_money
        print ("Ohh that's not good, " + user_name + " lose " + str (bet_money) + ". " + user_name + "'s total money is: " + str (money)+ "\n" + "-"*100)
        if money <= 0:
            print (user_name + "'s money is $" + str (money) + "\n" + user_name + "Lose :( ")
            # again = input ("Do wanna play again: Y or N:  ")
            # if again.upper () == "Y":
            #     Play_Game_Number_Guess ()
            # else:
            End ()


#print(Dice_Comp("Normal"))  ## for test

time.sleep(3)
if difficulty == "Easy":
    print (user_name + " welcome to THROWING THE DICE " + difficulty + " part.\n" + '-' * 100 + "\nYou get your money from  Flip the Coin.\nIn this game we have 2 dices. You and computer throw the dice separately and if the dice number is bigger than computer. You win.\nBut it's important if number of dices multiplied by each other, your money multiply or divide by this dices ratio.\nIf you get your money ten times bigger you pass this level. if you get your money under $50 you lose\nGood luck!!!\n" + "-" * 100)

    time.sleep(5)
    dice_user = 0
    dice_comp = 0
    win_money = money * 10

    while money < win_money:
        dice_comp = Dice_Comp ("Easy")
        if dice_comp > 4:
            dice_comp = Dice_Comp ("Easy")
        dice_user_str = input (user_name + " throw your dice (press D): ")
        if dice_user_str.upper () != "D":
            while dice_user_str.upper () == "D":
                dice_user_str = input (user_name + " for throw your dice please (press D): ")

        dice_user = Dice_Comp ("Easy")
        print (user_name + "'s dice  : " + str (dice_user))
        print ("Computer dice  : " + str (dice_comp))

        if dice_user == dice_comp:
            print ("!!! Tie !!! No win no lose. " + user_name + "'s money is: $" + str (money) + "\n" + "=" * 100)

        elif dice_user > dice_comp:
            multiply = round (dice_user / dice_comp)
            money = round (money * multiply)
            # print(multiply) ##for test
            print ("Today is your day, " + user_name + "'s total money is $" + str (money) + "\n" + "=" * 100)
            if money >= win_money:
                print ("*" * 50 + "\n!!! " + user_name + " Win !!!\n" + user_name + "'s money is: $" + str (money) + "\n" + "*" * 50)

        else:
            divide = round (dice_comp / dice_user)
            money = round (money / divide)
            # print (divide) ##for test
            print ("Sorry " + user_name + " lost some money, " + user_name + "'s total money is $" + str (money))
            if money < 50:
                print (user_name + "'s money is $" + str (money) + ".\n" + user_name + " Lose :( ")
                # again = input ("Do wanna play again: Y or N:  ")
                # if again.upper () == "Y":
                #     Play_Game_Number_Guess ()
                #     else:
                End ()

if difficulty == "Normal":
    print (user_name + " welcome to THROWING THE DICE " + difficulty + " part.\n" + '-' * 100 + "\nYou get your money from  Flip the Coin.\nIn this game we have 2 dices. At first  dices aggregate and then second dice multiply this Aggregation. Who gets the 250 first will win the game get money doubled.\nGood luck!!!\n" + "-" * 100)

    dice_user1 = random.choice (Dice_Comp ("Normal"))[0]
    dice_user2 = random.choice (Dice_Comp ("Normal"))[1]

    total_user = 0
    total_comp = 0
    finish = False

    while finish == False: 
        dice_comp1 = random.choice (Dice_Comp ("Normal"))[0]
        dice_comp2 = random.choice (Dice_Comp ("Normal"))[1]

        dice_user1 = input (user_name + " throw your FIRST dice (press D): ")
        if dice_user1.upper () != "D":
            while dice_user1.upper () == "D":
                dice_user1 = input ("For throw your FIRST dice please (press D): ")
                dice_user1 = random.choice (Dice_Comp ("Normal"))[0]
        dice_user1 = random.choice (Dice_Comp ("Normal"))[0]

        dice_user2 = input (user_name + " throw your SECOND dice (press D): ")
        print ("-" * 50)
        if dice_user2.upper () != "D":
            while dice_user2.upper () == "D":
                dice_user2 = input ("For throw your SECOND dice please (press D): ")
                print ("-" * 50)
        dice_user2 = random.choice (Dice_Comp ("Normal"))[1]

        print (user_name + "'s dices are : " + str (dice_user1) + ", " + str (dice_user2))
        print ("Computer dices are : " + str (dice_comp1) + ", " + str (dice_comp2))

        total_comp = (dice_comp1 + dice_comp2) * dice_comp2 + total_comp
        print ("-" * 50 + "\nComputer total number is : " + str (total_comp))
        total_user = (dice_user1 + dice_user2) * dice_user2 + total_user
        print (user_name + "'s total number is : " + str (total_user) + "\n" + "-" * 50)

        if total_user >= 250:
            money *= 2
            print ("*" * 50 + "\nCongratulations " + user_name + " win!!!\n" + user_name + "'s money is: $" + str (money))
            print("*"*100)
            finish = True
        if total_comp >= 250:
            print (user_name + "'s money is $" + str (0) + ".\n" + user_name + " Lose :( ")
            # again = input ("Do wanna play again: Y or N:  ")
            # if again.upper () == "Y":
            #     Play_Game_Number_Guess ()
            # else:
            End ()

if difficulty == "Hard":
    print (user_name + " welcome to THROWING THE DICE " + difficulty + " part.\n" + '-' * 100 + "\nYou get your money from  Flip the Coin. Also computer have same money as you.\nIn this game we have 2 dices. Your first dice multiply computer money and second divide computer's money.\nComputer's dices are make the same issue on your money. After 5 tour if you have money bigger than computer you get your money doubled. If not you lose.\nGood luck!!!\n" + "-" * 100)

    dice_user1 = random.choice (Dice_Comp ("Normal"))[0]
    dice_user2 = random.choice (Dice_Comp ("Normal"))[1]

    TotalMoneyUser = 0
    TotalMoneyComp = 0
    tour = 1

    while tour < 6:
        dice_comp1 = random.choice (Dice_Comp ("Normal"))[0]
        dice_comp2 = random.choice (Dice_Comp ("Normal"))[1]

        dice_user1 = input (user_name +" throw your FIRST dice (press D): ")
        if dice_user1.upper () != "D":
            while dice_user1.upper () == "D":
                dice_user1 = input ("For throw your FIRST dice please (press D): ")
                dice_user1 = random.choice (Dice_Comp ("Normal"))[0]
        dice_user1 = random.choice (Dice_Comp ("Normal"))[0]

        dice_user2 = input ("Throw your SECOND dice (press D): ")
        print ("-" * 50)
        if dice_user2.upper () != "D":
            while dice_user2.upper () == "D":
                dice_user2 = input ("For throw your SECOND dice please (press D): ")
                print ("-" * 50)
        dice_user2 = random.choice (Dice_Comp ("Normal"))[1]

        print ("Computer dices are : " + str (dice_comp1) + ", " + str (dice_comp2))
        print (user_name + "'s dices are : " + str (dice_user1) + ", " + str (dice_user2))
       
        TotalMoneyComp = (dice_user1 * money) + round (money / dice_user2) + TotalMoneyComp
        print ("-" * 50 + "\nComputer total money is : $" + str (TotalMoneyComp))
        TotalMoneyUser = (dice_comp1 * money) + round (money / dice_comp2) + TotalMoneyComp
        print (user_name + " total money is : $" + str (TotalMoneyUser) + "\n" + "-" * 50)

        if tour == 5:
            if TotalMoneyUser >= TotalMoneyComp:
                if money >= TotalMoneyUser:
                    money *= 2
                    print ("*" * 100 + "\nCongratulations " + user_name + " win!!!\n" + user_name + "'s total money is: $" + str (money))
                    print("*" * 100)
                else:
                    TotalMoneyUser *= 2
                    print ("*" * 100 + "\nCongratulations " + user_name + " win!!!\n" + user_name + "'s money is: $" + str (TotalMoneyUser))
                    print ("*" * 100)
                    money = TotalMoneyUser
            else:
                print (user_name + "'s money is $" + str (0) + ".\n" + user_name + " Lose :( ")
                # again = input ("Do wanna play again: Y or N:  ")
                # if again.upper () == "Y":
                #     Play_Game_Number_Guess ()
                # else:
                End ()

        tour += 1


time.sleep(3)
print("="*100)
'''Play MathGame'''
print(user_name + ", Math game is about solving a math problem. Answer 5 question correctly and\nmake your money double in easy, trible in normal and quintuple in hard difficulty. Good luck, make your best\n" + "+-=/*"*20)
time.sleep(5)
''' Get 5 question randomly from MathQuiz.py '''
quizbank = []

if difficulty == "Easy":
    while 6 > len (quizbank):
        quiz = random.choice (MathQuiz.Easy)
        if quiz not in quizbank:
            quizbank.append (quiz)

elif difficulty == "Normal":
    while 6 > len (quizbank):
        quiz = random.choice (MathQuiz.Normal)
        if quiz not in quizbank:
            quizbank.append (quiz)

elif difficulty == "Hard":
    while 6 > len (quizbank):
        quiz = random.choice (MathQuiz.Hard)
        if quiz not in quizbank:
            quizbank.append (quiz)

time.sleep(5)
tour = 0
while tour < len (quizbank)- 1:
    print ("Question " + str (tour + 1) + ": " + quizbank[tour][0])
    answer = quizbank[tour][1]
    #print(answer) ## for test when playing close this code
    answer_user = input (user_name + " please write your answer: ")
    time.sleep(1)
    if answer == int (answer_user):
        if difficulty == "Easy":
            money = 2 * money

        elif difficulty == "Normal":
            money = 3 * money

        elif difficulty == "Hard":
            money = 5 * money

    print (user_name + "'s answer is True" + user_name + "'s total money is $" + str(money) + "\n" + "-"*50)
    time.sleep(2)
    if tour == len(quizbank) - 2:
        print ("*"*100 + "\n" + "*"*3 + user_name + " it's end of the game." + "*"*3 + "\n" + "*"*3 + user_name + "'s total money is $" + str(money) + "*"*3 + "\n" + "-" * 100)

    tour += 1

con = sqlite3.connect("record.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS game_best (name TEXT, age INT, score INT)")
cursor.execute("INSERT INTO game_best(name, age, score) VALUES( ?, ?, ?)", (user_name, user_age, money))
cursor.execute("SELECT name, age, score FROM game_best ORDER BY score ASC")
data = cursor.fetchall()
for score in data:
    print(score)
con.commit ()
con.close()

