from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FALSE_BUTTON_PATH = 'images/false.png'
TRUE_BUTTON_PATH = 'images/true.png'
FONT = ('Arial', 20, 'italic')

false_button_image, true_button_image = 0, 0


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.main_window = Tk()
        self.main_window.title("Quiz Time!")
        self.main_window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text((150, 125), text="Question Text",
                                                     fill=THEME_COLOR, font=FONT, width=290)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.main_window.mainloop()

    def get_next_question(self):
        """
        This function will call the next_question() method from the quiz_brain.py file.
        :return: None
        """

        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)

        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ended.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_button_pressed(self):
        """
        This function changes the question to next question and checks the answer.
        :return: None
        """

        self.give_result(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        """
        This function changes the question to next question and checks the answer.
        :return: None
        """

        self.give_result(self.quiz.check_answer("False"))

    def give_result(self, is_right):
        """
        This function checks whether the user gave the correct answer or not and changes the background
        color accordingly.
        :param is_right: boolean
        :return: None
        """

        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.main_window.after(1000, self.get_next_question)
