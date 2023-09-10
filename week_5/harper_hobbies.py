"""
    Title: harper_hobbies.py
    Author: James Harper
    Date: 9 September 2023
    Description: Python Conditionals, Lists, and Loops.
"""

hobbies = ["Moutain Biking", "Brewing", "Gaming", "Wood Working", "Coding"]

for item in hobbies:
    print(item)
    
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for item in days:
    if item == "Sunday" or item == "Saturday":
        print(str(item) + ". Day off! Time to enjoy some hobbies.")
    else:
        print(str(item) + ". Uhg! It's a work day.")