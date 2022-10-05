"""
The first program of Programming 01 2022
Name: Gianmarco Ipinze Tutuianu <gianmarco.ipinzetutuianu@tuni.fi>
StudentId: 151456655

"""

validInputs = ["Y", "y", "N", "n"]


def main():
    
    n = input("Bored? (y/n) ")

    while n not in validInputs[0:2]:
        if n not in validInputs[2:]:
            n = input("Incorrect entry.\nPlease retry: ")
        else:
            n = input("Bored? (y/n) ")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()