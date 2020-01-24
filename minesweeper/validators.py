class GameValidator(object):
    def validateSettings(self, height, width, numberOfMines):
        if height not in range(3, 31) and width not in range(3, 31):
            raise ValueError("Height and width must be 3-30")
        if numberOfMines not in range((height+width)//2, int(0.5 * height * width)):
            raise ValueError("Number of mines must be at least the arithmetic sum of the two dimensions and at most half of the total number of tiles")
