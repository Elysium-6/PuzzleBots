

class map_cell:

    def __init__(self, top, bot, left, right, number):
        self.top = top
        self.bot = bot
        self.left = left
        self.right = right
        self.number = number
        self.traversed = False