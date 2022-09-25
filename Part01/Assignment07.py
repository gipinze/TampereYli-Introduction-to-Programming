def main():
    cost = int(input("Purchase price: "))
    pay = int(input("Paid amount of money: "))
        
    change = pay-cost
    
    if change > 0:
        print("Offer change:")
        
        if (change//10 != 0):    
            print(change//10, "ten-euro notes")
            change = change%10
        if (change//5 != 0):
            print(change//5, "five-euro notes")
            change = change%5
        if (change//2 != 0):
            print(change//2, "two-euro coins")
            change = change%2
        if (change//1 != 0):
            print(change//1, "one-euro coins")
            
    else:
        print("No change")
    
if __name__ == "__main__":
    main()
