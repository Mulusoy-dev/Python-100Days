from OOP_project import Question
from OOP_data import question_data
from OOP_final import QuizBrain


q=[]
a=[]

for i in question_data:
    q.append(i["text"])
    a.append(i["answer"])

# print(q[0])
# print(a[0])
question_bank=[]

for i in range(len(q)):
    question_bank.append(Question(q[i], a[i]))
    
# print(question_bank)

# for k in range(len(q)):
#     print(question_bank[k].text)
#     print(question_bank[k].answer)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


