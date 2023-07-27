print("Welcome to python pizza deliveres! ")
size = input("what size pizza do you want? S , M, or L ")
add_bzar = input("Do you want bzar? Yes or No ")
fromage = input("Do you want extra cheese? Yes or No ")

bill = 0
if size == "S":
    bill += 15
elif(size == "M"):
    bill += 20
else:
    bill += 25

if add_bzar == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3
if fromage == "Yes":
    bill += 1

print(f"Your final bill is ${bill}")
cancel_order = input("If you want to cancel your order click Y :")

if cancel_order == "Y":
    bill = ""
    size = ""
    print("Your order canceled :)!")
else:
    print("thanks for the order")