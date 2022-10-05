"""
COMP.CS.100 Programming 1.
Programming 01 - 2022
Name: Gianmarco Ipinze Tutuianu <gianmarco.ipinzetutuianu@tuni.fi>
StudentId: 151456655
Solution 3.6.1 - The song: "Old MacDonald"
"""

def print_verse(animal, onomatopoeia):
    """
    Prints the parameters for the song based on the animals given in the example doc
    Ex. 
        Animal = cow
        onomatopoeia = moo
    
    """
    print(f"""Old MACDONALD had a farm\nE-I-E-I-O\nAnd on his farm he had a {animal}\nE-I-E-I-O\nWith a {onomatopoeia} {onomatopoeia} here\nAnd a {onomatopoeia} {onomatopoeia} there\nHere a {onomatopoeia}, there a {onomatopoeia}\nEverywhere a {onomatopoeia} {onomatopoeia}\nOld MacDonald had a farm\nE-I-E-I-O""")


def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()