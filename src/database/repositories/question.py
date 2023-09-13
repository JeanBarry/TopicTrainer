from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import SQLAlchemyError

from src.database import Database
from src.database.models import Question
from src.database.validators import validate_question_creation


class QuestionRepository:
    """
    QuestionRepository class to manage the operations of the Question model.
    """

    def __init__(self):
        self.database = Database()

    def get_all(self) -> list[Question]:
        """
        Get all questions.

        :return: The questions
        """
        session = self.database.get_session()
        questions = session.query(Question).all()
        session.close()
        return questions

    def get_by_id(self, question_id: UUID) -> Question:
        """
        Get a question by its id.

        :param question_id: The resource id
        :return: The question
        """
        session = self.database.get_session()
        question = session.query(Question).filter_by(id=question_id).first()
        session.close()
        return question

    def get_by_topic_id(self, topic_id: UUID) -> list[Question]:
        """
        Get all questions by topic id.

        :param topic_id: The topic id
        :return: The questions
        """
        session = self.database.get_session()
        questions = session.query(Question).filter_by(topic_id=topic_id).all()
        session.close()
        return questions

    def create(self, **kwargs) -> Question or None:
        """
        Create a question.

        :param kwargs: The question attributes

        The question attributes are:
            topic_id: The topic id
            text: The question text

        :return: The created question
        """

        if not validate_question_creation(kwargs):
            print("Invalid question attributes")
            return None

        question = Question(**kwargs)

        with self.database.get_session() as session:
            try:
                session.add(question)
                session.commit()
                session.refresh(question)
                return question
            except SQLAlchemyError as error:
                session.rollback()
                print(f"Error creating question: {error}")
                return None
