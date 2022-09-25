# A program that determines user's age group (if-statement).
    # Read the age as a string and convert it to an integer.
 

def main():
    input1 = input("Player 1, enter your choice (R/P/S): ")
    input2 = input("Player 2, enter your choice (R/P/S): ")
    
    player1 = str(input1)
    player2 = str(input2)
    
    
    if player1 == "R" and player2 == "P":
        print("Player 2 won!")
    elif player1 == "P" and player2 == "S":
        print("Player 2 won!")
    elif player1 == "S" and player2 == "R":
        print("Player 2 won!")
    elif player1 == player2:
        print("It's a tie!")
    else:
            print("Player 1 won!")
    
if __name__ == "__main__":
    main()
