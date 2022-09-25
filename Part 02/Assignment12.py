def main():
    
    n = int(input("Choose a number: "))
    
    i = 1
    
    calc = True
    
    while calc:
        
        result = i * n
        
        print(i,"*",n,"=", result)
        i += 1
        
        if result >= 100:
            calc = False
            
if __name__ == "__main__":
    main()
