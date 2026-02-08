
from python.day17.data import questions_and_answers


class Question:
    """Attributes Text : question,answer :True/False"""
    def __init__(self,q_text,q_answer):
        self.q_text=q_text
        self.q_answer=q_answer

