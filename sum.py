"""
Author: Paul Sommers
Date written: 10/28/2024
Assignment: Exercise 3-9
Short Desc: This program receives numbers from the user as input and calculates the sum and average. 
"""

# Initialize variables
theSum = 0.0
count = 0

# Begin our Loop
while True:
    # Prompt user for input
    userInput = input("Enter a number or press enter to quit: ")

    # Check if the input is blank
    if userInput == "":
        break

    # Convert to a float and add to the sum
    number = float(userInput)
    theSum += number
    count += 1

# Display the sum
print(f"\nThe sum is {theSum}")

# Display the average if at least one number was submitted
if count > 0:
    average = theSum / count
    print(f"The average is {average}")
else:
    print("No numbers were entered.")