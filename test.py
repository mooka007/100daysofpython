# ************************* High Score ******************************* #

# studentScore = [31,22,33,44,55,66,77,88,99,23,65,87,54,52,76]
# highestScore = 0

# for score in studentScore:
#     if score > highestScore:
#         highestScore = score
# print(f"The highest score in the class is : {highestScore}")

# *************************** Adding Even Numbers ****************************** #


# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# total2 = 0
# for num in range(1, 101):
#     if num % 2 == 0:
#         total2 += num
# print(total2)


# *************************** Fizz Buzz ****************************** #

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# *************************** paint area ****************************** #

# import math

# def paint_calc(height, width, cover):
#     area = height * width
#     numofcans = math.ceil(area / cover)
#     print(f"you will need {numofcans} cans of painting")


# test_h = int(input("Height of wall : "))
# test_w = int(input("Width of wall : "))
# coverRage = 5
# paint_calc(height=test_h, width=test_w, cover=coverRage)

# *************************** prime checker ****************************** #

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime == False
#     if is_prime:
#         print("its a prime number.")
#     else:
#         print("its not a prime number")

# n = int(input("Check this Number : "))
# prime_checker(number=n)



# *************************** prime checker ****************************** #

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"
    
# print(student_grades)


# ***************************  Class user ****************************** #

# class User:
    
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
    
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user_1 = User("001", "angela")
# user_2 = User("002", "karma")

# user_1.follow(user_2)
# user_2.follow(user_1)
# print(user_1.followers)
# print(user_1.following)












