"""
COMP.CS.100 Programming 1.
Programming 01 - 2022
Name: Gianmarco Ipinze Tutuianu <gianmarco.ipinzetutuianu@tuni.fi>
StudentId: 151456655
Solution 3.6.2 - The song "Yogi the bear"
"""

def verse(verse, character):
    
    """ Prints the song verses"""
    print(verse)
    print(f'{character}, {character}', sep=", ")
    print(verse)
    repeat_name(character, 3)
    print(verse)
    repeat_name(character, 1)
    
    
def repeat_name(character, repetition):
    
    """Mentions the character and the times of it's repetition"""
    for _ in range(repetition):
        print(f'{character}, {character} Bear')


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
