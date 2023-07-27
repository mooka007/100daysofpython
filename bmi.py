height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2, 2)

print(f"Your Bmi  is {bmi}")

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight. ")
elif(bmi > 18.5 and bmi < 25):
    print("you have a normal weight")
elif(bmi > 25 and bmi <30 ):
    print("you are overweight ")
elif(bmi > 30 and bmi < 35):
    print("you are obese")
else:
    print("you are clinically obese")