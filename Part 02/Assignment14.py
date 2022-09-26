def main():
    
    n = int(input("How many numbers would you like to have? "))
    
    for i in range(1, n+1):
        
        condition1 = i % 3 == 0
        condition2 = i % 7 == 0
        
        if condition1 and condition2:
            print("zip boing")
        elif condition1:
            print("zip")
        elif condition2:
            print("boing")
        else:
            print(i)


if __name__ == "__main__":
    main()
