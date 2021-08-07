from os import system
board = [' ']*9

def print_board():
    global board
    
   # system("clear")
    loop = 0
    while loop <3:
        
        print(board[loop*3]+'|'+board[1+loop*3]+'|'+board[2+loop*3])
       
        if loop == 0 or loop ==1:
            print("-+-+-")
        loop += 1

isXTurn = False
x = 'x'
o = 'o'

def what_is_available():
    global board
    
    a = []
    for piece in range(len(board)):
        if board[piece] == ' ':
            a.append(piece)
    return a
        
def if_available(n):
    global board, available
    
    avail = False
    if n in available:
        avail = True
    return avail

def see_available():
    global available
   #system("clear")
   # print_board()
    print("Available: {}".format(available))

available = what_is_available()

def change_turn():
    global isXTurn
    
    isXTurn = not isXTurn
    
def whose_turn():
    global isXTurn     
    
    trn = 'o'
    if isXTurn:
        trn = 'x'
    return trn

def place_piece():
    global board
    
  #  t = whose_turn()
    see_available()
    response = input("What positoin would you like to play (0-8) : ")
    
   #Check if response is a number
    while not response.isdigit():
            see_available()
            response = int(input("Pease put number!!! \nx: what positoin would you like to play (0-8): "))
   #We knowresponse is a number(isdigit()) so we can work with it as a num
    response = int(response)
        
    try:
        while not(0 <= response <= 8) or not if_available(response):
            see_available()
            
            response = int(input("x: what positoin would you like to play (0-8): "))
       
        board[response] = 'x'
    except ValueError:
        print("Error")
        place_piece()
        
def win():
    win = False
    t = whose_turn()
    
    for i in range(3):
        if board[i+3]== t and board[1+i+3]== t and board[2+i+3]== t:
            win = True
            break
    if not win:
        for i in range(3):
            if board[i] == t and board[i+3] == t and board[i+6] == t:
                win = True
                break
    if not win: 
        if board[0] == t and board[4] == t and board[8] == t or board[6] == t and board[4] == t and board[2] == t:
            win = True
            
    if win:
        print('win for: {}'.format(t))
    return win
def is_cats_game():
     is_draw = True
     count = 0
     while count < 9 :
         if board[count]== ' ':
             is_draw = False
             break
         count =+1
     return is_draw

def play_again():
    
    global board, isXTurn
    stay = False
    
    response = input("Do you want to play again?  (Y/N): ").upper()
    while response != 'Y' and response != 'N':
        system('clear')
        response = input("Do you want to play again?  (Y/N): ").upper()
        
    if response == 'Y':
        stay = True
        board = [' ']*9
        isXTurn = False
        
    return stay


while True:
    
    print_board()
    available = what_is_available()
    place_piece()
    
    if win():
        print_board()
        
        if isXTurn:
            print('X wins!')
        else:
            print('O wins!')
        if play_again():
            continue
        else:
            print('Good Game')
            break
    elif is_cats_game():
        print("Cates GAME")
        
        if play_again():
            continue
        else:
            print('Good Game')
            break
    else:
        change_turn()
            
        
        
    