def main():
    
    n = int(input("How many numbers would you like to have? "))
    
    i = 1
    
    while n >= 1:
        # every time the next number is divisible by 3 the player has to say "zip"
        if i % 3 == 0 and i % 7 != 0:
            print("zip")
            n += (-1)
            i += 1
            
        # every time the number is divisible by 7 the player has to say "boing". 
        elif i % 7 == 0 and i % 3 !=0:
            print("boing")
            i += 1
            n += (-1)

        # if the number is divisible by both the numbers, the player should say "zip boing".
        elif i % 3 == 0 and i % 7 == 0:
            print("zip boing")
            i += 1
            n += (-1)
            
        else:
            print(i)
            i += 1
            n += (-1)

if __name__ == ("__main__"):
    main()
