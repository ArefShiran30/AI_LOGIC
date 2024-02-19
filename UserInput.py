
import Logic

def inputs_before_move():
    '''This function take input from the user'''
    newlist = []
    for x in range(2):
        newlist.append(int(input()))
    for x in range(2):
        newlist.append(input())
    return newlist #List of inputs [4,4,B,>]



def visual_input(rowNum:int)->list:
    '''This function take visual input and then
    return list that we work on it in whole program '''
    new_list = []
    for rownumber in range(rowNum):
        x = input().split()
        new_list.append(x)
    return new_list

def move_input()->list:
    '''take move from the user and return it as list'''
    player_input = input().split(' ')
    return player_input


def playGame():
    '''This function doing game in user interface'''
    x = inputs_before_move()
    z = visual_input(x[0])
    y = Logic.OthelloGame(z, len(z), len(z[0]), x[2], x[3])
    while True:
        if not y.check_if_game_can_continue():
            y.declare_winner()
            break
        if not y.check_if_player_can_continue():
            y.toggle_player()
            continue
        else:
            y.show_info()
        while True:
            m = move_input()
            if y.Total_valid(m):
                print('VALID')
                break
            else:
                print('INVALID')
        y.Filip(m)
        y.toggle_player()


if __name__ == "__main__":
    print("FULL")
    playGame()
