from OOP_project import Question



class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)
       

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")







# score=0
# quiz = QuizBrain(0, question_bank[0])
# user_a= input(f"Q.1. {quiz.question_list.text} (True/False)?: ")
# state=1

# if quiz.question_list.answer == user_a:
#     score += 1
#     print("You got it right!")
#     print(f"The correct answer was {quiz.question_list.answer}")
#     print(f"Your current score is: {score}")

# else:
#     print("That's wrong.")
#     print(f"The correct answer was {quiz.question_list.answer}")
#     print(f"Your current score is: {score}")












# quiz = QuizBrain(0, question_bank[1])
# user_a= input(f"Q.1. {quiz.question_list.text} (True/False)?: ")
# #user_a = input("(True/False)?:")

# if quiz.question_list.answer == user_a:
#     score += 1
#     print("You got it right!")
#     print(f"The correct answer was {quiz.question_list.answer}")
#     print(f"Your current score is: {score}")

# else:
#     print("That's wrong.")
#     print(f"The correct answer was {quiz.question_list.answer}")
#     print(f"Your current score is: {score}")







# print(quiz.question_list.text)
# print(quiz.question_list.answer)



