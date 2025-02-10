class QuizBrain:
    def __init__(self,question_list):
        self.question_number =0
        self.question_list= question_list
        self.score = 0
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
       
       
    def next_question(self):
        the_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q{self.question_number+1}: {the_question.text} (true/false) >>> ")
        self.check_answer(user_answer,the_question.answer)
            

    def check_answer(self,user_answer,the_answer):
        if user_answer.lower() == the_answer.lower():
           self.score+=1
           print(f"GG its Right")
        else:
            print("wrong")
        
        print(f"the correct answer was : {the_answer}\nYour score is: {self.score}/{self.question_number}\n")
