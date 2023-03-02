
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    # To print board
    print(f"{board[0]} | {board[1]} | {board[2]}     1 | 2 | 3")
    print(f"{board[3]} | {board[4]} | {board[5]}     4 | 5 | 6")
    print(f"{board[6]} | {board[7]} | {board[8]}     7 | 8 | 9")

current_player = "X" 
game_running = True  

def play_game(): 
    display_board()
    while game_running:
        handle_turn(current_player)
        check_win()
        flip_turn()
        
        
def handle_turn(player):
    print(f"It's {player} turn ")
    position = int(input(f"choose the postion from 1-9: ")) 
    while board[position - 1] != "-":
        print("Positon already occupied")
        position = int(input(f"choose the postion from 1-9 "))
    board[position-1] = player
    display_board()

def check_win():
    global game_running
    column_win = check_column()
    row_win = check_row()
    daignol_win = check_daignol()
    if column_win or row_win or daignol_win == True:
        print(f"Yay {current_player} won the game! ")
        game_running = False   
    elif "-" not in board:
        print("Tie")
        game_running = False
    


def check_row():
    row1= board[0] == board[1] == board[2] != "-"
    row2= board[3] == board[4] == board[5] != "-"
    row3= board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3 :
        return True
    

def check_column():
    column1= board[0] == board[3] == board[6] != "-"
    column2= board[1] == board[4] == board[7] != "-"
    column3= board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3 :
        return True
    

def check_daignol():
    daignol1= board[0] == board[4] == board[8] != "-"
    daignol2= board[2] == board[4] == board[6] != "-"
    if daignol1 or daignol2 :
        return True
    

def flip_turn():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()