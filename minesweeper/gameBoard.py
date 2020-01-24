class GameBoard(object):
    def __init__(self, height = 10, width = 10, numberOfMines = 10):
        self._height = height
        self._width = width
        self._numberOfMines = numberOfMines
        self._board = []

    @property
    def Board(self):
        return self._board

    @Board.setter
    def Board(self, otherBoard):
        self._board = otherBoard

    @property
    def Height(self):
        return self._height

    @Height.setter
    def Height(self, otherHeight):
       self._height = otherHeight

    @property
    def Width(self):
        return self._width

    @Width.setter
    def Width(self, otherWidth):
        self._width = otherWidth

    @property
    def NumberOfMines(self):
        return self._numberOfMines

    @NumberOfMines.setter
    def NumberOfMines(self, otherNumberOfMines):
        self._numberOfMines = otherNumberOfMines

    @property
    def VisualBoardComplete(self):
        visualBoard = ""
        for rowCoordinate in range(self._height):
            for columnCoordinate in range(self._width):
                visualBoard += self._board[rowCoordinate][columnCoordinate].VisualRepresentation + " "
            visualBoard += "\n"
        return visualBoard

    @property
    def VisualBoardForPlayer(self):
        visualBoard = ""
        for rowCoordinate in range(self._height):
            for columnCoordinate in range(self._width):
                if self._board[rowCoordinate][columnCoordinate].Status == "discovered":
                    visualBoard += self._board[rowCoordinate][columnCoordinate].VisualRepresentation + " "
                elif self._board[rowCoordinate][columnCoordinate].Status == "marked":
                    visualBoard += ">" + " "
                else:
                    visualBoard += "O" + " "
            visualBoard += "\n"
        return visualBoard

    def validateMarkFlag(self, rowCoordinate, columnCoordinate):
        if self._board[rowCoordinate][columnCoordinate].Status == "marked":
            raise ValueError("Tile already marked with flag")
        if self._board[rowCoordinate][columnCoordinate].Status == "discovered":
            raise ValueError("Tile has been discovered and cannot be marked with flag")

    def validateUnmarkFlag(self, rowCoordinate, columnCoordinate):
        if self._board[rowCoordinate][columnCoordinate].Status != "marked":
            raise ValueError("Tile not marked with flag")

    def validateMarkSafeTile(self, rowCoordinate, columnCoordinate):
        if self._board[rowCoordinate][columnCoordinate].Status == "marked":
            raise ValueError("Tile marked with flag. Remove the flag first to mark this tile as safe")
        if self._board[rowCoordinate][columnCoordinate].Status == "discovered":
            raise ValueError("You have already marked this tile as safe")

    def markFlag(self, rowCoordinate, columnCoordinate):
        '''
        marks the tile as flagged
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        self.validateMarkFlag(rowCoordinate, columnCoordinate)
        self._board[rowCoordinate][columnCoordinate].Status = "marked"
        #self._board[rowCoordinate][columnCoordinate].VisualRepresentation = ">"

    def unmarkFlag(self, rowCoordinate, columnCoordinate):
        '''
        marks the tile as unflagged
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        self.validateUnmarkFlag(rowCoordinate, columnCoordinate)
        self._board[rowCoordinate][columnCoordinate].Status = "undiscovered"

    def markSafeTile(self, rowCoordinate, columnCoordinate):
        '''
        marks the tile as safe
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        self.validateMarkSafeTile(rowCoordinate, columnCoordinate)
        self._board[rowCoordinate][columnCoordinate].Status = "discovered"

    def surroundingTiles(self, rowCoordinate, columnCoordinate):
        '''
        :param rowCoordinate: the row coordinate of the tile
        :param columnCoordinate: the column coordinate of the tile
        :return: a list with the surrounding tiles
        '''
        listOfTiles  = []
        if rowCoordinate == 0:
            if columnCoordinate == 0:
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate])
            elif columnCoordinate == self._width - 1:
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate])
            else:
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate])
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate - 1])
        elif rowCoordinate == self._height - 1:
            if columnCoordinate == 0:
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate])
            elif columnCoordinate == self._width - 1:
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate])
            else:
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate])
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate - 1])
        else:
            if columnCoordinate == 0:
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate])
            elif columnCoordinate == self._width - 1:
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate])
            else:
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate + 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate])
                listOfTiles.append(self._board[rowCoordinate - 1][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate][columnCoordinate - 1])
                listOfTiles.append(self._board[rowCoordinate + 1][columnCoordinate - 1])
        return listOfTiles

    def numberOfSurroundingMines(self, rowCoordinate, columnCoordinate):
        '''
        computes the number of mines in surrounding tiles
        :param rowCoordinate: the row coordinate
        :param columnCoordinate: the column coordinate
        :return: the number of mines in surrounding tiles
        '''
        numberOfSurroundingMines = 0
        for tile in self.surroundingTiles(rowCoordinate, columnCoordinate):
            if tile.Value == "mine":
                numberOfSurroundingMines += 1
        return numberOfSurroundingMines

    def autoFillInitialize(self):
        '''
        it sets the SearchedThrough attribute of all tiles to False
        because the autoFillRecursive function is recursive, in order to prevent a maximum recursion depth exceeded,
        we make sure that we only expand to the tiles that haven't already been "searched through"
        :return:
        '''
        for rowCoordinate in range(self._height):
            for columnCoordinate in range(self._width):
                self._board[rowCoordinate][columnCoordinate].SearchedThrough = False

    def autoFillRecursive(self, rowCoordinate, columnCoordinate):
        '''
        fills in all the tiles according to the player's tile choice (recursively)
        :param rowCoordinate:
        :param columnCoordinate:
        :return: the tiles are discovered
        '''
        if self._board[rowCoordinate][columnCoordinate].Status == "discovered": #we have already beeen in this tile
            return

        if self._board[rowCoordinate][columnCoordinate].Status == "marked": #the player has a flag on this tile, so we won't reveal it
            return

        if not (rowCoordinate in range(self._height) and columnCoordinate in range(self._width)): #list indices out of range
            return

        self._board[rowCoordinate][columnCoordinate].Status = "discovered"
        self._board[rowCoordinate][columnCoordinate].SearchedThrough = True

        if self._board[rowCoordinate][columnCoordinate].Value != None: #the tile has numerical value
            return
        else:
            try:
                self.autoFillRecursive(rowCoordinate, columnCoordinate + 1)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate + 1, columnCoordinate + 1)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate + 1, columnCoordinate)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate + 1, columnCoordinate - 1)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate, columnCoordinate - 1)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate - 1, columnCoordinate - 1)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate - 1, columnCoordinate)
            except IndexError:
                pass
            try:
                self.autoFillRecursive(rowCoordinate - 1, columnCoordinate + 1)
            except IndexError:
                pass

    def autoFill(self, rowCoordinate, columnCoordinate):
        '''
        the complete autoFill function, using the autoFillInitialize and autoFillRecursive
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        self.validateMarkSafeTile(rowCoordinate, columnCoordinate)
        self.autoFillInitialize()
        if self._board[rowCoordinate][columnCoordinate].Value == "mine":
            self._board[rowCoordinate][columnCoordinate].Status = "discovered"
            return
            #GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!
        self.autoFillRecursive(rowCoordinate, columnCoordinate)