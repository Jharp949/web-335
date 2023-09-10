"""
    Title: harper_hobbies.py
    Author: James Harper
    Date: 9 September 2023
    Description: Python Conditionals, Lists, and Loops.
"""

#List containing 5 hobbies. 
hobbies = ["Moutain Biking", "Brewing", "Gaming", "Wood Working", "Coding"]

#Loop that iterates through each item in the hobbies list.
for item in hobbies:
    print(item)

#List of days of the week.     
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Loop through each item in days, prints the day to the terminal with a custom message.
for item in days:
    if item == "Sunday" or item == "Saturday":
        print(str(item) + ". Day off! Time to enjoy some hobbies.")
    else:
        print(str(item) + ". Uhg! It's a work day.")