from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import SQLAlchemyError

from src.database import Database
from src.database.models import Answer
from src.database.validators import validate_answer_creation


class AnswerRepository:
    """
    AnswerRepository class to manage the operations of the Answer model.
    """

    def __init__(self):
        self.database = Database()

    def get_all(self) -> list[Answer]:
        """
        Get all answers.

        :return: The answers
        """
        session = self.database.get_session()
        answers = session.query(Answer).all()
        session.close()
        return answers

    def get_by_id(self, answer_id: UUID) -> Answer:
        """
        Get an answer by its id.

        :param answer_id: The resource id
        :return: The answer
        """
        session = self.database.get_session()
        answer = session.query(Answer).filter_by(id=answer_id).first()
        session.close()
        return answer

    def get_by_question_id(self, question_id: UUID) -> list[Answer]:
        """
        Get all answers by question id.

        :param question_id: The question id
        :return: The answers
        """
        session = self.database.get_session()
        answers = session.query(Answer).filter_by(question_id=question_id).all()
        session.close()
        return answers

    def get_correct_answer_by_question_id(self, question_id: UUID) -> Answer:
        """
        Get the correct answer by question id.

        :param question_id: The question id
        :return: The answer
        """
        session = self.database.get_session()
        answer = session.query(Answer).filter_by(question_id=question_id, is_correct=True).first()
        session.close()
        return answer

    def create(self, **kwargs):
        """
        Create an answer.

        :param kwargs: The answer attributes

        The answer attributes are:
            question_id: The question id
            text: The answer text
            is_correct: The answer is correct
        """
        if not validate_answer_creation(kwargs):
            print("Invalid answer attributes")
            return None

        answer = Answer(**kwargs)

        with self.database.get_session() as session:
            try:
                session.add(answer)
                session.commit()
                session.refresh(answer)
                return answer
            except SQLAlchemyError as error:
                session.rollback()
                print(f"Error creating answer: {error}")
                return None
