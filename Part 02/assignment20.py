daysMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    
    for month in range(1, 13):
        
        for days in range(1, daysMonths[month-1]+1):
            print(f"{days}.{month}.", sep="")


if __name__ == "__main__":
    main()
