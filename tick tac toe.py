# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:10:39 2025

@author: ahmed
"""

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    return None

def is_board_full(board):
    return " " not in board

def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter positions (1-9) as shown below:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("\nLet's start!\n")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                position = int(input("Enter position (1-9): ")) - 1
                if 0 <= position <= 8:
                    if board[position] == " ":
                        break
                    else:
                        print("That position is already taken!")
                else:
                    print("Please enter a number between 1 and 9!")
            except ValueError:
                print("Please enter a valid number!")
        
        board[position] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break