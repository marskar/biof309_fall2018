# ideas to warp strategies https://www.quantamagazine.org/the-game-theory-math-behind-rock-paper-scissors-20180402/

def janken_bot():
    """
    User plays takes on JANKEN_BOT in a traditional game of rock, paper, sissors.

    Input:
        name (str): user is prompted to input name
        weapon (int): user selects weapon 1,2, or 3
            0 = rock
            1 = paper
            2 = scissors

    TODO:
    - add check for proper input
    - new hight score report
    - keep only top 10 high scores

    """
    print('"Who dares to take on the JANKEN_BOT?!"')
    print()
    name = input('Input name: ')

    # taunt
    print()
    print('"' + name + ', prepare to meet your DOOM!!!"')
    print()

    # packages used
    import random
    import pandas as pd

    # counters
    weapons = [0, 1, 2]
    translation = ['rock','paper','scissors']
    win_count = 0
    score = 0
    round_count = 1

    # print directions

    while True:
        # report round
        # "\n" creats a new line
        print()
        print("--- ROUND " + str(round_count) + " ---")

        # weapon select
        player_weapon = int(input('Select weapon: \n 1. rock \n 2. paper \n 3. scissors \n')) - 1
        machine_weapon = random.choice(weapons)

        # print message of selected weapons
        print()
        print(name + ": " + str(translation[player_weapon]))
        print("JANKEN_BOT: " + str(translation[machine_weapon]))
        print()

        # determine outcome
        dif = player_weapon - machine_weapon
        # tie
        if player_weapon == machine_weapon:
            round_count += 1
            score += 1 + win_count
            print("TIE, on to the next round!\n")
        # player wins
        elif (dif == 1 or dif == -2):
            round_count += 1
            score += 10 * win_count
            win_count += 1
            print("YOU WON!!!")
        # player looses
        else:
            player_status = 0
            print("Bummer, you're janken days are over")
            break
    print()
    print("Number of Wins: " + str(win_count))
    print("Final Score: " + str(score))

    # pandas high scores
    # import the 'high_scores.csv' as a Pandas dataframe
    df = pd.read_csv('high_scores.csv')
    # insert the latest score into index position -1
    df.loc[-1] = [name,score,win_count]
    # sort the dataframe by 'score'
    df = df.sort_values(by=['score'], axis=0, ascending=False)
    # reset the dataframe index to start with 0
    df = df.reset_index(drop=True)
    # print the top 5 high scores
    print(df.head(5))
    # save the dataframe as a .csv
    df.to_csv('high_scores.csv', index=False)
    
