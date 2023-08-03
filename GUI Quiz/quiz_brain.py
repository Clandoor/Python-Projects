import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        This function checks whether the questions are still there or not.
        :return: bool
        """
        
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        This function fetches the next question from the list and returns an fstring.
        :return: String
        """
        
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def check_answer(self, user_answer):
        """
        This function the answer.
        :return: bool
        """
        
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
