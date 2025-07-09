#QuizGame
#Use opentdb.com for more trivia qustions
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text}\nTrue or False?"
        )
        correct_answer = current_question.answer
        self.check_answer(answer, correct_answer)

    def still_has_questions(self, question_list):
        return self.question_number < (len(question_list))

    def check_answer(self, answer, correct_answer):
        if answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The current score is {self.score}/{len(self.question_list)}")


# ----------------------------------------------------------------------------
from data import quiz_questions

question_bank = []

for item in quiz_questions:
    question_bank.append(Question(item["text"], item["answer"]))

q = QuizBrain(question_bank)

while q.still_has_questions(question_bank):
    answer = q.next_question()
    print("\n")

print("You've completed the Quiz.")
print(f"Your final score is {q.score}/{len(question_bank)}")