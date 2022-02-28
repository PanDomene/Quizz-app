from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Aquí van las preguntas", width=280,
                                                fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number-1}")
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz. "
                                                       f"Your score was {self.quiz.score}/{self.quiz.question_number}")
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, color: str):
        self.canvas.config(bg=color)
        self.window.after(1000, self.canvas.config, {"bg": "white"})
        self.window.after(1000, self.get_next_question)
