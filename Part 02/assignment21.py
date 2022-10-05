def main():
    
    friday = 0
    
    for month in range(1,13):
                

        if month == 2:
            last_day = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            last_day = 30
        else:
            last_day = 31
            
        # Prints the dates
        for day in range(1,last_day+1):
            
            # Adds one more "friday"
            friday +=  1 
            
            #IF friday is divisible for 7 giving 3 as result (3%7=3, 10%7=3, 17%7=3)
            if friday % 7 == 3:
                print(f"{day}.{month}.", sep="")

if __name__ == "__main__":
    main()
