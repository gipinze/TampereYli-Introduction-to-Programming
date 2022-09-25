def main():
    # The flag variable is initialized to True to start the loop.
    

    # Read words while the value of the flag variable is True.
    while True:
        word = input("Answer Y or N: ")
        if word in ("y", "n", "N", "Y"):
            break
        print("Incorrect entry.")
        # Flip the flag value to end the loop.
    print("You answered", word)

if __name__ == "__main__":
    main()
