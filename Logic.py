

EMPTY = '.'
WHITE = 'W'
BLACK = 'B'



class OthelloGame():
    '''This is the class that all the logic happened inside '''


    def __init__(self,board:list,row:int,col:int,turn:str,winner:str):
        self._board = board
        self._row =row
        self._col = col
        self._turn = turn
        self._winner = winner

    def set_turn(self,player:str):
        self._turn = player

    def toggle_player(self):
        '''This function toggle player'''
        if self._turn == BLACK:
            self._turn = WHITE
            return
        elif self._turn == WHITE:
            self._turn = BLACK
            return
    def get_opposite(self):
        '''This function change opposite turn'''
        if self._turn == BLACK:
            return WHITE
        else:
            return BLACK
    def get_turn(self):
        '''Just get turn'''
        return self._turn



    def check_filled(self,moveList:list):
        '''This function check that player select empty place '''
        if int(moveList[0])- 1<0 or int(moveList[1])- 1<0:
            return False
        row_number = int(moveList[0])-1
        col_number = int(moveList[1])-1
        if self._board[row_number][col_number] == EMPTY:
            return True
        else:
            return False





#For move check we need to check 8 different directions
# and if one of these direction works then this move is valid
#So we need to define 8 different functions in our class
#Also I need to make flip function from these functions()


    def valid_vertical_South_to_North(self,moveList) -> bool:
        '''this function check validity from south to north '''

        #valid_list = []
        number = 1 # This number increase each time we could flip our
        row_number = int(moveList[0])-1
        col_number = int(moveList[1])-1
        while (row_number - number) >= 0 and self._board[row_number - number][col_number] == self.get_opposite():

            number += 1
        if row_number - number >= 0 and self._board[row_number - 1][col_number] != self._turn  and \
                self._board[row_number - number][col_number] == self._turn:

            return True
        else:
            return False

    def valid_vertical_North_to_South(self,moveList) -> bool:
        '''this function check validity from north to south '''
s
        number = 1 # This number increase each time we could flip our
        row_number = int(moveList[0])-1
        col_number = int(moveList[1])-1
        while (row_number + number) < len(self._board) and self._board[row_number + number][col_number] == self.get_opposite():
            number += 1
        if row_number + number < len(self._board) and self._board[row_number + 1][col_number] != self._turn and \
        self._board[row_number + number][col_number] == self._turn:
            #valid_list.append(moveList)
            return True
        else:
            return False


    def valid_horizontal_west_to_east(self, moveList) -> bool:
        '''this function check validity from west to east '''

        number = 1  # This number increase each time we could flip our
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1
        while col_number + number < len(self._board[0]) and self._board[row_number][col_number + number] == self.get_opposite():

            number += 1
        if col_number + number < len(self._board[0]) and self._board[row_number][col_number +1] != self._turn \
                and  self._board[row_number][col_number + number] == self._turn:
            return True
        else:

            return False

    def valid_horizontal_east_to_west(self, moveList) -> bool:
        '''this function check validity from East to West '''
        number = 1  # This number increase each time we could flip our
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1
        while col_number - number >= 0 and self._board[row_number][col_number - number] == self.get_opposite():
            number += 1
        if col_number - number >= 0 and  self._board[row_number][col_number - 1] != self._turn and \
        self._board[row_number][col_number - number] == self._turn:

            return True
        else:
            return False

    def diagonal_South_East(self, moveList: list) -> bool:
        '''this function check validity from south to East '''
        number = 1  # This number increase each time we could flip our
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1
        while row_number + number < len(self._board) and col_number + number < len(self._board[0]) and \
        self._board[row_number + number][col_number + number] == self.get_opposite():

            number += 1
        if row_number + number < len(self._board) and col_number + number < len(self._board[0]) \
                and self._board[row_number + 1][col_number + 1] != self._turn and \
                self._board[row_number + number][col_number + number] == self._turn:
            return True
        else:
           return False

    def diagonal_North_West(self,moveList:list) -> bool:
        '''this function check validity from North to West '''
        number = 1 # This number increase each time we could flip our
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1
        while row_number - number >= 0 and col_number - number >= 0 and \
                        self._board[row_number - number][col_number - number] == self.get_opposite() :

            number += 1
        if row_number - number >= 0 and col_number - number >= 0 and \
                        self._board[row_number - 1][col_number - 1] != self._turn and \
                        self._board[row_number - number][col_number - number] == self._turn:
            return True
        else:
            return False

    def diagonal_North_East(self, moveList: list) -> bool:
        '''this function check validity from North to East '''
        number = 1  # This number increase each time we could flip our
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1

        while row_number - number >= 0 and col_number + number < len(self._board[0]) and \
                        self._board[row_number - number][col_number + number] == self.get_opposite():

            number += 1
        if row_number - number >= 0 and col_number + number < len(self._board[0]) and \
                self._board[row_number - 1][col_number + 1] != self._turn and \
                self._board[row_number - number][col_number + number] == self._turn :
            return True
        else:
            return False

    def diagonal_South_West(self,moveList: list) -> bool:
        '''this function check validity from south to west '''
        number = 1  # This number increase each time we could flip our
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1

        while row_number + number < len(self._board) and col_number - number >= 0 and \
        self._board[row_number + number][col_number - number] == self.get_opposite():

            number += 1
        if row_number + number < len(self._board) and col_number - number >= 0 \
                and self._board[row_number + 1][col_number - 1] != self._turn \
                and self._board[row_number + number][col_number - number] == self._turn:
            return True
        else:
            return False



    def flip_horizontal(self,moveList:list):
        '''this function flip horizontally'''

        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1


        if self.valid_horizontal_east_to_west(moveList) == True:
            self._board[row_number][col_number] = self._turn
            number = 1
            while col_number - number >= 0 and \
                self._board[row_number][col_number - number] == self.get_opposite():
                self._board[row_number][col_number - number] = self._turn
                number += 1

        if self.valid_horizontal_west_to_east(moveList) == True:
            number = 1
            self._board[row_number][col_number] = self._turn
            while col_number + number < len(self._board[0]) and \
                self._board[row_number][col_number + number] == self.get_opposite():
                self._board[row_number][col_number + number] = self._turn
                number += 1


    def flip_vertical(self, moveList: list):
        '''This function flip vertically'''

        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1

        if self.valid_vertical_South_to_North(moveList) == True:
            self._board[row_number][col_number] = self._turn
            number = 1
            while row_number - number >= 0 and self._board[row_number - number][col_number] == self.get_opposite():
                self._board[row_number - number][col_number] = self._turn
                number += 1


        if self.valid_vertical_North_to_South(moveList) == True:
            number = 1
            self._board[row_number][col_number] = self._turn
            while row_number + number < len(self._board[row_number]) and \
                self._board[row_number + number][col_number] == self.get_opposite():
                self._board[row_number + number][col_number] = self._turn
                number += 1



    def flip_diagonal(self, moveList: list):
        '''This function flip diagonally'''
        row_number = int(moveList[0]) - 1
        col_number = int(moveList[1]) - 1


        if self.diagonal_North_West(moveList) == True:
            self._board[row_number][col_number] = self._turn
            number = 1
            while col_number - number >= 0 and row_number - number >= 0 and \
                            self._board[row_number - number][col_number - number] == self.get_opposite():
                self._board[row_number - number][col_number - number] = self._turn
                number += 1

        if self.diagonal_South_East(moveList) == True:
            self._board[row_number][col_number] = self._turn
            number = 1
            while row_number + number < len(self._board) and \
                                    col_number + number < len(self._board[0]) and \
                            self._board[row_number + number][col_number + number] == self.get_opposite():
                self._board[row_number + number][col_number + number] = self._turn
                number += 1

        if self.diagonal_North_East(moveList) == True:
            self._board[row_number][col_number] = self._turn
            number = 1
            while row_number - number >= 0 and col_number + number >= 0 and \
                            self._board[row_number - number][col_number + number] == self.get_opposite():
                self._board[row_number - number][col_number + number] = self._turn
                number += 1

        if self.diagonal_South_West(moveList) == True:
            self._board[row_number][col_number] = self._turn
            number = 1
            while row_number + number < len(self._board[row_number]) and col_number - number >= 0 \
                    and self._board[row_number + number][col_number - number] == self.get_opposite():
                self._board[row_number + number][col_number - number] = self._turn
                number += 1


    def Filip(self,moveList):
        '''This function is for flip'''
        self.flip_diagonal(moveList)
        self.flip_horizontal(moveList)
        self.flip_vertical(moveList)


    def Total_valid(self,moveList):
        '''this function check all of the condition to make valid moves '''
        m = moveList
        if self.check_filled(m) and  (self.valid_vertical_North_to_South(m)
                                          or self.valid_vertical_South_to_North(m)
                                          or self.valid_horizontal_west_to_east(m)
                                          or self.valid_horizontal_east_to_west(m)
                                          or self.diagonal_North_East(m)
                                          or self.diagonal_North_West(m)
                                          or self.diagonal_South_East(m)
                                          or self.diagonal_South_West(m)):
            return True
        else:
            return False
    def check_if_game_can_continue(self):
        '''Check if the game can continue'''
        player = self._turn
        check1 = self.check_if_player_can_continue()
        self.toggle_player()
        check2 = self.check_if_player_can_continue()
        self._turn = player
        return (check1 or check2)

    def check_if_player_can_continue(self):
        '''Check if player can continue'''
        for i in range(0,len(self._board)):
            for j in range(0,len(self._board[0])):
                check = self.Total_valid([i+1,j+1])
                if check:
                    return True
        return False
    def declare_winner(self):
        '''This function show us who is winner'''
        numB = self.count_black()
        numW = self.count_white()
        if self._winner == ">":
            if numB>numW:
                print("B: " + str(numB) + "  " + "W: " + str(numW))
                self.visualize_board()
                print("WINNER: B")
                return
            elif numW<numB:
                print("B: " + str(numB) + "  " + "W: " + str(numW))
                self.visualize_board()
                print("WINNER: W")
                return
            else:
                print("B: " + str(numB) + "  " + "W: " + str(numW))
                self.visualize_board()
                print("WINNER: NONE")
                return
        elif self._winner == "<":
            if numB<numW:
                print("B: " + str(numB) + "  " + "W: " + str(numW))
                self.visualize_board()
                print("WINNER: B")
                return
            elif numW>numB:
                print("B: " + str(numB) + "  " + "W: " + str(numW))
                self.visualize_board()
                print("WINNER: W")
                return
            else:
                print("B: " + str(numB) + "  " + "W: " + str(numW))
                self.visualize_board()
                print("WINNER: NONE")
                return
        return

    def count_black(self):
        count = 0
        for i in range(0,len(self._board)):
            for j in range(0,len(self._board[0])):
                if self._board[i][j] == "B":
                    count = count + 1
        return count

    def count_white(self):
        count = 0
        for i in range(0,len(self._board)):
            for j in range(0,len(self._board[0])):
                if self._board[i][j] == "W":
                    count = count + 1
        return count
    def visualize_board(self):
        for i in range(0,len(self._board)):
            string = " ".join(self._board[i])
            print(string)
    def show_info(self):
        numW = self.count_white()
        numB = self.count_black()

        print("B: " + str(numB) +"  "+ "W: " + str(numW))
        self.visualize_board()
        print("TURN: " + self.get_turn())
