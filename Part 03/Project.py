def main():
    
    month = 1
    max_dif = 0 
    odd_month = 0.0
    even_month = 0.0
    inflation_input = ""
    
    dif_list=[]
    
    """ For loops are better when we know the amount of times the iteration is going to be repeated """
    """ While loops are better when we DO NOT KNOW the amount of times """
    
    
    while True:
        
        # To read the inflation input
        inflation_input = input(f"Enter inflation rate for month {month}: ")
        
        # This lines are to create 2 different inputs to storage within the list and later compare them
        
        if inflation_input != "":
            
            if month % 2 == 1:
                
                odd_month =  float(inflation_input)
                
                dif_list.append(odd_month)

            else:
                even_month = float(inflation_input)

                dif_list.append(even_month) # this line add the values to the list
        
        dif = [dif_list[i + 1] - dif_list[i] for i in range(len(dif_list)-1)] # This line allows me to knows the difference between the values within the list
        
        max_dif = max(dif, default=0) # Selects the "biggest" value, which means that, if it is negative, the closes to 0 is the biggest
        
        month +=1
        
        # print(dif_list)
        
        if inflation_input == "":
            if month <=3:
                print("Error: at least 2 monthly inflation rates must be entered.")
            else:
                # print(dif)
                print(f"Maximum inflation rate change was {max_dif:.1f} points.")
            break        
        
        
    # for max_dif in dif_list:
    #     print("Differences are: ", float(max_dif))
        
if __name__ == "__main__":
    main()
