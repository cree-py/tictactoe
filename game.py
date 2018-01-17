# Tic Tac Toe Game

import random

board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "

chars = ['x', 'o']

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_for_solution(board, list):
    '''Method that checks for a solution.'''
    if 1 in list:
        if 2 in list:
            if 3 in list:
                return True
            else:
                return False
        elif 4 in list:
            if 7 in list:
                return True
            else:
                return False
        elif 5 in list:
            if 9 in list:
                return True
            else:
                return False
    elif 2 in list:
        # List doesn't contain 1 and therefore match across top is ruled out
        if 5 in list:
            if 8 in list:
                return True
            else:
                return False
        else:
            return False
    elif 3 in list:
        # List doesn't contain 1 or 2 and therefore match across top is ruled out
        if 5 in list:
            if 7 in list:
                return True
            else:
                return False
        elif 6 in list:
            if 9 in list:
                return True
            else:
                return False
        else:
            return False
    elif 4 in list:
        # List doesn't contain 1, 2, or 3 and therefore match left column is ruled out
        if 5 in list:
            if 6 in list:
                return True
            else:
                return False
        else:
            return False
    elif 5 in list:
        # List doesn't contain 1, 2, 3 or 4 and therefore everything is ruled out
        return False
    elif 6 in list:
        # List doesn't contain 1, 2, 3, 4 or 5 and therefore everything is ruled out
        return False
    elif 7 in list:
        # List doesn't contain 1, 2, 3, 4, 5 or 6 and therefore match left column and 
        # top right to bottom left are ruled out
        if 8 in list:
            if 9 in list:
                return True
            else: 
                return False
        else:
            return False
    elif 8 in list:
        # List doesn't contain 1, 2, 3, 4, 5, 6 or 7 and therefore everything is ruled
        # out
        return False
    elif 9 in list:
        # List doesn't contain 1, 2, 3, 4, 5, 6, 7 or 8 and therefore everything is
        # ruled out
        return False
    else:
        return False

try:
    playerchar = input('Choose your marker: ')
    if playerchar.lower() == 'x':
        playerchar = 'x'
        compchar = 'o'
        print("X is selected.")
    elif playerchar.lower() == 'o':
        playerchar = 'o'
        compchar = 'x'
        print("O is selected.")
    else:
        playerchar = random.choice(chars)
        if playerchar == "x":
            compchar = "o"
        else:
            compchar = "x"
        print(f"Invalid input. Your randomly selected marker will be {playerchar}.")
except Exception as e:
    print(f"Error: {e}")

index = random.randint(0, 1)

if index == 0:
    print("Player has been selected to go first!")
    isPlayerTurn = True
else:
    print("Computer has been selected to go first!")
    isPlayerTurn = False

gameIsOver = False

userList = []
compList = []

print(board)

while not gameIsOver:
    if isPlayerTurn:
        if check_for_solution(board, compList):
            winner = "Computer"
            break
        invalid = True
        while invalid:
            if not nums:
                winner = "Nobody"
                break
            move = input('Make your move.\n>')
            try:
                move = int(move)
            except:
                pass
            if move not in nums:
                
                print("Invalid selection. Please try again.")
            else:
                print("Move selected!")
                invalid = False
        userList.append(move)
        try:
            board = board.replace(str(move), playerchar)
            nums.remove(move)
        except:
            winner = "Nobody"
            break
        print(board)
        isPlayerTurn = False
        if check_for_solution(board, userList):
            winner = "User"
            break
        continue
    else:
        if check_for_solution(board, userList):
            winner = "User"
            break
        print("Computer is thinking...")
        try:
            move = random.choice(nums)
            board = board.replace(str(move), compchar)
            nums.remove(move)
            compList.append(move)
        except Exception as e:
            if check_for_solution(board, userList):
                winner = "User"
            elif check_for_solution(board, compList):
                winner = "Computer"
            else:
                winner = "Nobody"
            print(e)
            break
        print(board)
        isPlayerTurn = True
        if check_for_solution(board, compList):
            winner = "Computer"
            break
        continue

print(f"The winner is {winner}!")