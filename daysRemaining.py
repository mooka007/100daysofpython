# this code takes user input for their current age and calculates how many days, weeks, 
# and months they have left until they reach the age of 90.
age = input("What is your current age? ")


ageAsInt = int(age)
years_remaining = 90 - ageAsInt
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

msg = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(msg)