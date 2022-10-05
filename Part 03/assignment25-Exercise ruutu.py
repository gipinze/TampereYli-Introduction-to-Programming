def print_box(width, height, mark):
    
    """   prints a box with the expected dimensions """
    
    for _ in range(height):
        print(mark*width)
        
        
def readInput(message):
    
    """ Reads the input (which must be and integer) and if it is less or equals 0, 
        then repeats the message (asks for the width/height value again)"""
        
    otp = int(input(message))
    while otp <= 0:
        otp = int(input(message))
    return otp
    

def main():
    width = readInput("Enter the width of a frame: ")
    height = readInput("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
