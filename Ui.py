from tkinter import *
from Quiz_game_brain import QuizBrain


THEME_COLOR = "#375362"
RED = "#FF3333"
GREEN = "#008000"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_board = Label(text="Score: 0", fg="white",
                                 bg=THEME_COLOR,
                                 font=("Arial", 18, "bold"))
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150,125,width= 280,
                                                text="some question ",
                                             font=("Franklin Gothic Medium Cond", 20,"italic"),
                                             fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.correct_click)
        self.true.grid(row=2, column=1)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0,command=self.wrong_click)
        self.false.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def correct_click(self):
        is_correct = self.quiz.check_answer("True")
        self.feedback(is_correct)

    def wrong_click(self):
        is_correct = self.quiz.check_answer("False")
        self.feedback(is_correct)

    def feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)