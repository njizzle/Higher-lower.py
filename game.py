from random import randint

# Dice and score
DICE = ["❶", "❷", "❸", "❹", "❺", "❻"]
finalscore = 0



print("welcome to higher or lower lets roll")

def play(finalscore):
    def roll():
        dice_num = randint(0, 5)
        return dice_num
    
    def run(user, computer, input, score):
        if input == 1:
            if user >= computer:
                print(f"computer score is {DICE[computer]} you get a point ")
                score += 1
                return score
                
            else:
                print(f"computer score is {DICE[computer]}")
                return score

        elif input == 2:
            if user < computer:
                print(f"computer score is {DICE[computer]} you get a point ")
                score += 1
                return score
            else:
                print(f"computer score is {DICE[computer]}")
                return score

    player1 = roll()
    computer = roll()

    print(f"you rolled {DICE[player1]}")

    choice = int(input("type 1 for higher or 2 for lower"))
    score = run(player1, computer, choice, finalscore)

    if score == finalscore:
        print("you lost")
        print(f"you had {finalscore} points")
    else:
        finalscore = score
        print(f"your on {finalscore} points")
        play(finalscore)



play(finalscore)
