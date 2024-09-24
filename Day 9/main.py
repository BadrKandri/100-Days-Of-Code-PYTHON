from question import Question
from data import question_data
from brain import QuizBrain

question_bank=[]

for item in question_data:
    new_text=item['question']
    new_answer=item['correct_answer']
    new_question=Question(new_text,new_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("you finished the QUIZ")
print(f"your score is {quiz.score}/{quiz.question_number+1}")
