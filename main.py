import os
import time
import random
from roster import *
from kickoff import kickoff

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def play():
    kickoff_instance = kickoff()
    down = 1
    if kickoff_instance.ball() == True:
        input("You have the ball, press enter to snap the ball. ")
        time.sleep(0.5)
        clear_terminal()
        print("SET HUT!")
        my_lineup.ball_holder = my_lineup.qb
        time.sleep(1)
        my_lineup = starting_lineup("Bartholomew Simpson", "Homer Griffin", "Bart Peterson", "Cricket Smith", "Moe Jones", "Bill Johnson", "Bartholomew Simpson")
        print(my_lineup.lineup)
        clear_terminal()
        print(starting_lineup.lineup)
        play_type = input("Press R and ENTER to hand the ball off to the running back. Press Q and ENTER to do a passing play. Press V and ENTER to run with QB. ")
        if play_type in ["r", "R"]:
            print("You handed the ball off to the running back.")
            time.sleep(1)
            clear_terminal()
            my_lineup.ball_holder = my_lineup.rb1
            print(f"{my_lineup.ball_holder} has the ball!")
            to_go = abs(100 - kickoff_instance.get_ball_start())
            yards_first = random.randint(6, to_go)
            if yards_first == to_go:
                print("TOUCHDOWN!")
            print(f"The running back ran for {yards_first} yards.")
            defense_positions = ["CB", "NT", "REND", "LEND", "LOLB", "MIDLIB", "ROLB", "FS", "SS"]
            print("Trucked by " + random.choice(defense_positions))
            ball2 = abs(100 - yards_first)
            print(f"The ball is now on the {ball2} yard line.")
        elif play_type in ["q", "Q"]:
            passing_play = input("Press Z and ENTER to pass to Z, Press X and ENTER to pass to X, Press Y and ENTER to pass to Y.")
            if passing_play in ["z", "Z"]:
                print(f"You passed to {my_lineup.z}.")
                time.sleep(1)
                chance = random.randint(1, 4)
                if chance == 1:
                    print("Intercepted by" + random.choice(defense_positions) + "!")
                elif chance == 2:
                    print("The pass was incomplete, now going into second down.")
                    down = 2
                    print(f"SCOREBOARD: 0 - 0, {2} and 10")
                elif chance == 3:
                    print("The receiver caught it, tacked by " + random.choice(defense_positions) + ", WHICH CAUSES A FUMBLE!!!")
                    fumble1 = random.randint(1, 2)
                    if fumble1 == 1:
                        print("The offense recovered the ball.")
                    elif fumble1 == 2:
                        print("THE DEFENSE TURNS IT OVER!")

    else:
        play_start = input("The other team has the ball, press enter to start the play. ")
    play = True


play()