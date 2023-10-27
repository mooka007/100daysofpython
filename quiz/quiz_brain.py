# TOdo : asking the question
#        checking if the answer is correct 
#        checking if we're the end  of the quiz

# Create a class called QuizBrain
# Write an __init__() method
# initialise the question_number to 0
# initialise the question_list to an input 

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True / False) : ")
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)