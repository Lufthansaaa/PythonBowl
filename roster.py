class starting_lineup:
    lineup = """X AOOCOOY Z

     QR"""
    
    def __init__(self, center, qb, rb1, z, y, x, ball_holder):
        self.center = center
        self.qb = qb
        self.rb1 = rb1
        self.z = z
        self.y = y
        self.x = x
        self.ball_holder = ball_holder
        print(starting_lineup.lineup)

class starting_defense:
    def __init__(self, lineup, nose_tackle, left_end, right_end, left_outside_linebacker, right_outside_linebacker, left_inside_linebacker, right_inside_linebacker, left_cornerback, right_cornerback, free_safety, strong_safety):
        self.lineup = """LEND NT REND
        
        CB LOLB MIDLIB ROLB CB
                    
                FS SS"""
        self.nose_tackle = nose_tackle
        self.left_end = left_end
        self.right_end = right_end
        self.left_outside_linebacker = left_outside_linebacker
        self.right_outside_linebacker = right_outside_linebacker
        self.left_inside_linebacker = left_inside_linebacker
        self.right_inside_linebacker = right_inside_linebacker
        self.left_cornerback = left_cornerback
        self.right_cornerback = right_cornerback
        self.free_safety = free_safety
        self.strong_safety = strong_safety
        print(lineup)