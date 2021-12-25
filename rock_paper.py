
#This game can easily be made using random.choice() method
#But this game is build using random.randint() method

import random

def score_board(player_score, computer_score, draw_match):
    scores = f"""
    :::::<Score Board>:::::
    Your Score:     {player_score}
    Computer Score: {computer_score}
    Draw Match:     {draw_match}
    """
    print(scores)
    if player_score > computer_score:
        print("<Congrats! You Won>")
    elif player_score < computer_score:
        print("<You Lose!>")
    else:
        print("<Match Is Draw>")

def print_selection(input_value, random_value):
    if input_value == 1 :
        print("<Player>     : Rock")
    elif input_value == 2:
        print("<Player>     : Paper")
    elif input_value == 3:
        print("<Player>     : Scissor")
    else:
        print("<Error>")

    if random_value == 1:
        print("<Computer>   : Rock")
    elif random_value == 2:
        print("<Computer>   : Paper")
    else:
        print("<Computer>   : Scissor")


def play():
    draw_match = 0
    player_score = 0
    computer_score = 0
    for i in range(5):
        random_value = random.randint(1, 3)

        message = """
        Select ->
        Rock    : 1
        Paper   : 2
        Scissor : 3 
        
        Enter here  : """
        input_value = int(input(message))
        print_selection(input_value, random_value)
        valid_input = (1, 2, 3)
        if input_value in valid_input and input_value == random_value:
            print("<Draw>")
            draw_match += 1
        elif input_value in valid_input:
            if (input_value == 1 and random_value == 3) or \
                    (input_value == 2 and random_value == 1) or \
                    (input_value == 3 and random_value == 2):
                        print("<You win>")
                        player_score += 1
            else:
                print("<Computer win>")
                computer_score += 1
        else:
            print("<Panelty> Not Valid Input")
            computer_score += 1
    score_board(player_score, computer_score, draw_match)

def wanna_play():
    ans = str(input("Wanna Play- y/n "))
    yes_ans = ["y", "Y", "yes", "YES", "Yes"]
    no_ans = ["n", "N", "no", "NO", "No"]
    if ans in yes_ans:
        play()
    elif ans in no_ans:
        print("Bye!")
        exit()
    else:
        print("<Error> Please give yes/no!")
        wanna_play()

if __name__ == "__main__":
    wanna_play()
