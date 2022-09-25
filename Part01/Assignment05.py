
# A program that determines user's age group (if-statement).
def main():
    # Read the age as a string and convert it to an integer.
    string = input("How do you feel? (1-10) ")
    feel = int(string)
    if feel > 0 and feel <= 10:
        
    # Determine the suitable smile group.
    
        if feel == 1:
            print("A suitable smiley would be :'(")
        
        elif feel < 4:
            print("A suitable smiley would be :-(")
            
        elif feel < 8:
            print("A suitable smiley would be :-|")

        elif feel > 7 and feel < 10:
            print("A suitable smiley would be :-)")
            
        else:
            print("A suitable smiley would be :-D")
    
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()
