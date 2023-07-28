print("Welcome to the love Calculator!")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

concat_string = name1 + name2
lower_string_concated = concat_string.lower()

t = lower_string_concated.count("t")
r = lower_string_concated.count("r")
u = lower_string_concated.count("u")
e = lower_string_concated.count("e")

true = t + r + u + e

l = lower_string_concated.count("l")
o = lower_string_concated.count("o")
v = lower_string_concated.count("v")
e = lower_string_concated.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your Score is {love_score}, You Go Togheter like Coke And Mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your Score is {love_score}, You are alright together.")
else:
    print(f"Your Score is {love_score}")