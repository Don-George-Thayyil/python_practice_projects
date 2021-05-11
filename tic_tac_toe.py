
def who_is_first(): #decides who plays first
    turn = None
    while not turn:
        ask = input("Do you want to start? y/n: ")    
        if ask == "y":
            return 1
        elif ask == "n":
            return 0
        else:
            print("Typo detected. Try again with y or n")
            continue
#---------------------
def is_my_turn(turn): #to decide who is playing next
    if turn % 2 == 0:
        return False
    else:
        return True
#---------------------
def create_board(): #initial board creation
    board = []
    key = 1
    for arr_num in range(3):
        sub_arr = []
        for elem_num in range(3):
            sub_arr.append(key)
            key += 1
        board.append(sub_arr)
    return board
#---------------------
def draw_board(): #to display created/updated board in a graphical way
    print("--------------")
    for array in board:
        for element in array:
            print("|",element,"|",end = "")
        print("\n--------------")
#---------------------
def update_board(move,sign): #to change board according to the moves of player/computer
    for arr in board:
        for element in arr:
            if element == move:
                arr_ind = board.index(arr)
                element_ind = arr.index(element)
                board[arr_ind][element_ind] = sign
#---------------------
def move_is_legit(move, sign = "X"): #to check if we are selecting available slots
    if move in free_field:
        free_field.remove(move)
        if sign == "O":
            player_moves.append(move)
        else:
            computer_moves.append(move)
        return True
    else:
        return False
#---------------------
def enter_value(): #to take input from the player
    move = input("Enter the number: ")
    if not move.isdigit():
        print("put in a number!")
        return enter_value()
    else:
        move = int(move)
        sign = "O"
        if move_is_legit(move,sign):
            return move
        else:
            print("Not the possible choice. Try again!")
            return enter_value()
#---------------------
def did_win(sign):  #to check if someoene won after every move
    if sign == "O" and len(player_moves)>2:
        for array in winning_matrix:
            count = 0
            for item in player_moves:
                if item in array:
                    count += 1 
            if count >= 3:
                return True
            else:
                continue 
        else:
            return False
    elif sign == "X" and len(computer_moves)>2:
        for array in winning_matrix:
            count = 0
            for item in computer_moves:
                    if item in array:
                        count += 1 
            if count >= 3:
                return True
            else:
                continue
        else:
            return False
    else:
        return False
#---------------------
def play_again(): #prompt to play again or exit
    while 1:
        ask = input("Want to play again? y/n: ")   
        if ask == "y":
            return True
        elif ask == "n":
            return False
        else:
            print("Typo detected. Try again with y or n")
            continue
#---------------------
def ai_decision(): #brain of the computer's moves
    if len(player_moves) < 1:
        if move_is_legit(lib[0]):
            return lib[0]
    elif len(player_moves) == 1:
        for i in range(9):
            if move_is_legit(lib[i]):
                return lib[i]
    elif len(computer_moves)>=2:
        dup_matrix1 = winning_matrix[:]
        for array in winning_matrix:
            count1 = 0
            for j in computer_moves:
                if j in array and array in dup_matrix1:
                    count1 += 1
            if count1 >= 2:
                dup_matrix1.remove(array)
                moved = [i for i in array if i not in computer_moves]
                if move_is_legit(moved[0]):
                    return moved[0]
    if len(player_moves) > 1:
        dup_matrix = winning_matrix[:]
        for win_array in winning_matrix:
            count = 0
            for plyrmove in player_moves:
                if plyrmove in win_array and win_array in dup_matrix:
                    count += 1
            if count >= 2:
                dup_matrix.remove(win_array)
                moved = [i for i in win_array if i not in player_moves]
                if move_is_legit(moved[0]):
                    return moved[0]
                
        else:
            for i in range(9):
                if move_is_legit(lib[i]):
                    return lib[i]

#-----variables-------
winning_matrix = [
    [1,2,3],
    [1,5,9],
    [3,5,7],
    [2,5,8],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [3,6,9]
] #this matrix has patterns that denote winning
lib = {0:5,1:1,2:3,3:7,4:9,5:2,6:4,7:6,8:8} #slots that define priority, 0 has highest priority
want_to_play = True #variable to make game start
#---------------------

while want_to_play:
    free_field = [1,2,3,4,5,6,7,8,9]
    computer_moves = []
    player_moves = []
    turn = who_is_first()
    somebody_win = False
    #print(turn)
    #want_to_play = False
    board = create_board()
    while not somebody_win and free_field:
        if(is_my_turn(turn)):
            #print("it worked")
            draw_board()
            sign = "O"
            move = enter_value()
            turn+=1
            update_board(move,sign)
            draw_board()
            if did_win(sign):
                print("yayee you won")
                somebody_win = True
                want_to_play = play_again()
                break         
        else:
            move = ai_decision()
            #move = number_generator(1,10)
            sign = "X"
            #if move_is_legit(move,sign):
            turn += 1
            update_board(move, sign)
            draw_board()
            if did_win(sign):
                print("Computer has won!!")                
                somebody_win = True
                want_to_play = play_again()
                break
            #print("cmptr play")
    else:
        print("Game is a tie")
        want_to_play = play_again()
