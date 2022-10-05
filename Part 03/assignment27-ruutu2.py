"""
COMP.CS.100 Programming 1.
Programming 01 - 2022
Name: Gianmarco Ipinze Tutuianu <gianmarco.ipinzetutuianu@tuni.fi>
StudentId: 151456655
Solution 3.8.2 - Printing a box and checking the inputs
"""


def print_box(width, height, mark):
    
    """   prints a box with the expected dimensions """
    
    for _ in range(height):
        print(mark*width)
        
        
def read_input(message):
    
    """ Reads the input (which must be and integer) and if it is less or equals 0, 
        then repeats the message (asks for the width/height value again)"""
        
    otp = int(input(message))
    while otp <= 0:
        otp = int(input(message))
    return otp
    

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
