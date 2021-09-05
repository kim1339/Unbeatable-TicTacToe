# an unbeatable Tic Tac Toe program where you (X) play against the computer (O)

options = ['1','2','3','4','5','6','7','8','9']
corners = [1, 3, 7, 9]
import random
# set-up of grid, board is a list
def Board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# this function will help set 'X' or 'O' to the specific space on the board
def Move(board, letter, move):
    board[move] = letter

def Winner(b, l):
    # returns True if that player has won
    # b instead of board and l instead of letter
    # I calculated that there are 8 winning cases total
    return ((b[7] == l and b[8] == l and b[9] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or 
    (b[1] == l and b[2] == l and b[3] == l) or 
    (b[7] == l and b[4] == l and b[1] == l) or 
    (b[8] == l and b[5] == l and b[2] == l) or 
    (b[9] == l and b[6] == l and b[3] == l) or 
    (b[7] == l and b[5] == l and b[3] == l) or 
    (b[9] == l and b[5] == l and b[1] == l)) 

def Copy(board):
    # duplicate of the board list that will later help computer figure out which move to make
    Board_2 = []
    for i in board:
        Board_2.append(i)
    return Board_2

def isSpaceFree(board, move):
    # returns True if the space is free on board
    # if not marked by X or O, board[move] equals an empty string
    return board[move] == ' '

def PlayerMove(board):
    move = ' '
    # if the player types in an invalid number or they type in a number they already have before, ask for their input again
    while move not in options or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    # important to use int function since initial input is a string and will cause an error otherwise
    return int(move)

def RandomMoveFromList(board,specific_list):
    # returns a valid, random move from the list of possible moves on the board
    # returns None if there is no valid move
    possibleMoves = []
    for i in specific_list:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    playerLetter = 'X'
    # algorithm for AI (more code than PlayerMove function)
    # first, check if we can win in the next move
    # loop goes through the 9 options
    for i in range(1, 10):
        copy = Copy(board)
        if isSpaceFree(copy, i):
            Move(copy, computerLetter, i)
            if Winner(copy, computerLetter):
                return i

    # check if the player could win on their next move, and block them by putting computer symbol there instead (beat them to it)
    for i in range(1, 10):
        copy = Copy(board)
        if isSpaceFree(copy, i):
            Move(copy, playerLetter, i)
            if Winner(copy, playerLetter):
                return i

    # if player didn't occupy a corner spot during their first move, computer can move to a corner
    if board[1] != 'X' and board[3] != 'X' and board[7] != 'X'and board[9] != 'X':
        move = RandomMoveFromList(board, corners)
        if move != None:
            return move
    else:
        if isSpaceFree(board, 5): 
            return 5

    # move on one of the sides.
    return RandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # returns True if every space on the board has been taken. Otherwise returns False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# start console-based game
# first, print instructions once
print('Unbeatable Tic Tac Toe game against the computer! \nYou, the player (X), will go first.\nThe computer (O) goes next.')
print('The board positions are as follows:')
print('   |   |')
print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
print('-----------')
print('   |   |')
print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
print('   |   |')
print('-----------')
print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
print('   |   |\n\n')

Repeat = True
while Repeat:
  try:
    # reset the board
    theBoard = [' '] * 10
    playerLetter = 'X'
    computerLetter = 'O'
    turn = 'player'
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # player's turn
            Board(theBoard)
            move = PlayerMove(theBoard)
            Move(theBoard, playerLetter, move)

            if Winner(theBoard, playerLetter):
                Board(theBoard)
                print('You won')
                Repeat = False
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    Board(theBoard)
                    print('Tie')
                    Repeat = False
                    gameIsPlaying = False
                else:
                    turn = 'computer'
        else:
            # computer's turn
            move = getComputerMove(theBoard, computerLetter)
            Move(theBoard, computerLetter, move)

            if Winner(theBoard, computerLetter):
                Board(theBoard)
                print('You lose')
                Repeat = False
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    Board(theBoard)
                    print('Tie')
                    Repeat = False
                    gameIsPlaying = False
                else:
                    turn = 'player'
  except IndexError:
    continue

