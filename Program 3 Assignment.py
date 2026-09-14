# Day of the Week
# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week, where
# 1 = Monday,
# 2 = Tuesday,
# 3 = Wednesday,
# 4 = Thursday,
# 5 = Friday,
# 6 = Saturday,
# and 7 = Sunday.


# Get input from the user
day_num = int(input("Enter a number in the range of 1 through 7: "))

# Assign the numbers to the days of the week
days_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday" }

# Pull out the day of the week using the input number and print the result
print(f"{day_num} = {days_dict[day_num]}")
