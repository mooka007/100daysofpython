
# asking the user to input the total bill amount, 
# the tip percentage, and the number of people splitting the bill. 
# It then calculates the tip amount, 
# the total bill amount (including tip), 
# and the final amount each person should pay. 
# Finally, it prints the final amount each person should pay, 
# rounded to two decimal places.
print("Welcome to the tip calculator!")
bill  = float(input("what was the total bill ? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))




tip_as_percent = tip / 100 # bach n7awlo tip to percent
total_tip = bill * tip_as_percent 
total_bill = bill +  total_tip
final_amount = round((total_bill) / people, 2)

print(f"Each person should pay: $${final_amount} ")