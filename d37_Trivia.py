import requests
import html
from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- CONFIG ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Segoe UI"
QUESTION_AMOUNT = 10


# ---------------------------- MODEL CLASSES ------------------------------- #
class Question:
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def get_current_question(self) -> Question:
        return self.question_list[self.question_number]

    def next_question(self):
        self.question_number += 1

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_input: str) -> bool:
        correct_answer = self.get_current_question().answer
        if user_input == correct_answer:
            self.score += 1
            return True
        return False


# ---------------------------- UI CLASS ------------------------------- #
class TriviaUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Score Label
        self.score_label = Label(
            text="Score: 0", font=(FONT_NAME, 15, "bold"), bg=BACKGROUND_COLOR
        )
        self.score_label.grid(column=1, row=0, columnspan=2)

        # Canvas for question
        self.canvas = Canvas(
            width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR
        )
        self.title_text = self.canvas.create_text(
            400, 263, text="Question", width=600, font=(FONT_NAME, 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        # Buttons
        self.false_img = self.load_image("wrong.png")
        self.true_img = self.load_image("right.png")

        self.false_button = Button(
            image=self.false_img, highlightthickness=0, command=self.handle_false
        )
        self.false_button.grid(row=2, column=0)

        self.true_button = Button(
            image=self.true_img, highlightthickness=0, command=self.handle_true
        )
        self.true_button.grid(row=2, column=1)

        self.display_question()

    def load_image(self, filename: str) -> ImageTk.PhotoImage:
        return ImageTk.PhotoImage(file=f"Resources/{filename}")

    def handle_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def handle_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct: bool):
        self.canvas.config(bg="green" if is_correct else "red")
        self.update_score()
        self.window.after(1000, self.next_step)

    def next_step(self):
        self.quiz.next_question()
        self.display_question()

    def display_question(self):
        self.canvas.config(bg=BACKGROUND_COLOR)
        if self.quiz.still_has_questions():
            question = self.quiz.get_current_question().text
            self.canvas.itemconfig(self.title_text, text=question)
        else:
            self.canvas.itemconfig(self.title_text, text="Game Over!")
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def run(self):
        self.window.mainloop()


# ---------------------------- MAIN PROGRAM ------------------------------- #
def fetch_questions(amount=QUESTION_AMOUNT) -> list[Question]:
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty=easy&type=boolean"
    res = requests.get(url, verify=False)
    data = res.json().get("results", [])
    return [Question(html.unescape(q["question"]), q["correct_answer"]) for q in data]


if __name__ == "__main__":
    question_bank = fetch_questions()
    quiz = QuizBrain(question_bank)
    app = TriviaUI(quiz)
    app.run()
