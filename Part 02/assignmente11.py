"""
The first program of Programming 01 2022
Name: Gianmarco Ipinze Tutuianu <gianmarco.ipinzetutuianu@tuni.fi>
StudentId: 151456655

"""

def main():

    n = int(input("Choose a number: "))

    # use for loop to iterate 10 times
    for i in range(1,11):
        print(i,'*',n,'=',i*n)
    
if __name__ == "__main__":
    main()