from html import unescape

class QuizBrain:
    def __init__(self,q_list):
        self.current_question = None
        self.questions_number   = 0
        self.question_list  = q_list
        self.score = 0

    def still_has_question(self):
        """This is used to check if there are still questions in the quiz."""
        if self.questions_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        """This is used to get the next question."""
        self.current_question = self.question_list[self.questions_number]
        self.questions_number += 1
        q_question = unescape(self.current_question.question)
        return f"Q.{self.questions_number}: {q_question}"


    def check_answer(self,user_answer):
        """This is used to get if the user's answer is correct and the same as the answer."""
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
