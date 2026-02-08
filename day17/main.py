from python.day17.qui import QUIZ
from  question import  Question
from  data import questions_and_answers


Question_bank=[]
for i in questions_and_answers['results']:
    Question_text =i["question"]
    Question_answer =i["correct_answer"]
    new_question = Question(Question_text,Question_answer)
    Question_bank.append(new_question)

qu =QUIZ(Question_bank)

while qu.still_has_question():
    qu.next_question()
print("You completed the  quiz")
print(f"Your final score is {qu.score} and {len(Question_bank)}")


