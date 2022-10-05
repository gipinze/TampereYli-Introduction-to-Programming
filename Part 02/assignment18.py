"""
The first program of Programming 01 2022
Name: Gianmarco Ipinze Tutuianu <gianmarco.ipinzetutuianu@tuni.fi>
StudentId: 151456655

"""


def main():
    
    fn = 0
    sn = 1
    
    
    n = int(input("How many Fibonacci numbers do you want? "))
    
    
    for i in range(1, n+1):
        nf = fn + sn
        print(f'{i}. {sn}')
        fn = sn
        sn = nf
    
    
if __name__ == "__main__":
    main()