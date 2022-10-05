"""
A program that determines user's age group by using a function.
"""

def determine_age_group(age):
    """Determine and return user's age group.

    :param age: int, user's age.
    :return: string, user's age group. Return value is None, if the age is
    smaller than zero or greater than 150 years.
    """
    # Initialize to None to shorten the selection structure, where it is
    # now enough to assign a value to this variable, when age is valid.
    age_group = None
    
    # Determine the age group.
    if age >= 0 and age <= 150:
        if age == 0:
            age_group = "baby"
        elif age < 7:
            # Age is between 1-6 years.
            age_group = "toddler"
        elif age < 18:
            # Age is between 7-17 years.
            age_group = "at school-age"
        elif age < 40:
            # Age is between 18-39 years.
            age_group = "young adult"
        elif age < 60:
            # Age is between 40-59 years.
            age_group = "middle-aged adult"
        elif age <= 150:
            # Age is between 60-150 years.
            age_group = "old"

    # Return age group or error code.
    return age_group

def main():
    # Read the age as a string and convert it to an integer.
    string = input("Please, enter your age: ")
    age = int(string)

    # Call the function with a parameter value given by the user
    # and assign return value to a variable.
    age_group = determine_age_group(age)
    
    # Print the result.
    if age_group != None:
        # Prevent the automatic printing of spaces.
        print("You are a ", age_group, ".", sep = "")
    else:
        print("Invalid age!")

if __name__ == "__main__":
    main()