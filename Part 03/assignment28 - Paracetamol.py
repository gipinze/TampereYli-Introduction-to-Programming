def calculate_dose(p_weight, doses_time, day_24_dose):
    
    """ Calculation for patients day doses """
    avg_dose = 15 * p_weight
    
    if day_24_dose >= 4000 or doses_time < 6:
        return 0
    
    if day_24_dose + avg_dose >= 4000:
        return avg_dose - ((day_24_dose + avg_dose) - 4000)
    
    else:
        if doses_time >=6:
            return avg_dose
        else:
            return 0


def main():
    
    """ Main function to read the input values and use the calculate_dose function"""
    
    p_weight = int(input("Patient's weight (kg): "))
    doses_time = int(input("How much time has passed from the previous dose (full hours): "))
    day_24_dose = int(input("The total dose for the last 24 hours (mg): "))
    
    dosage = calculate_dose(p_weight, doses_time, day_24_dose)
    print(f"The amount of Parasetamol to give to the patient: {dosage}")
    
    

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
    main()
