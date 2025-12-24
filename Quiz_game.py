from Quiz_game_data import data
from Quiz_game_question_model import Question
from Quiz_game_brain import QuizBrain
from Ui import QuizInterface



question_bank = []
for q in data:
    question_text   =q["question"]
    question_answer = q["correct_answer"]
    new_question    = Question(question = question_text, answer = question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
