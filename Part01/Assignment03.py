# Reading the student benefit.  The prompt is ended with whitespace
# so that the user input will not appear "touching" the colon.

input_line = input("Enter the amount of the study benefits: ")

# Converting the input_line into decimal number (float).
index = float(input_line)

# Conversion formula to add the first 1.17%.
new_value = (index * 1.0117)

# Conversion formula to add the second 1.17%.
second_value = (new_value * 1.0117)

# Printing out the Celsius result.
print("If the index raise is 1.17 percent, the study benefit, \nafter a raise, would be", new_value,
    "euros \nand if there was another index raise, the study \nbenefits would be as much as", second_value, "euros")
