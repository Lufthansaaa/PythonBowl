import random
class kickoff:
    def ball(self):
        ref_num = random.randint(1, 10)
        your_num = None
        while your_num is None:
            user_input = input("Pick a number between 1 and 10. ")
            if user_input.strip() == "":
                print("Please enter a number")
            else:
                try:
                    your_num = int(user_input)
                    if your_num < 1 or your_num > 10:
                        print("Please enter a number from 1 through 10: ")
                        your_num = None
                except ValueError:
                    print("Please enter a valid number.")
        other_team_num = random.randint(1, 10)
        your_diff = abs(ref_num - your_num)
        other_team_diff = abs(ref_num - other_team_num)

        if your_diff < other_team_diff:
            print("You got the ball!")
            self.ball_start = random.randint(24, 67)
            print(f"The ball will start at the {self.ball_start} yard line.")
            return True
        elif your_diff > other_team_diff:
            print("The other team got the ball!")
            return False
        else:
            print("It's a tie! Try again.")
            self.ball()

    def get_ball_start(self):
        return self.ball_start
