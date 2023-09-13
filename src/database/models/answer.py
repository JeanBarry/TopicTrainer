# pylint: disable=not-callable, too-few-public-methods
import uuid
from sqlalchemy import Column, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT, BOOLEAN
from src.database.models.common import Base


class Answer(Base):
    """
    Answer model
    Used to store answers to questions
    """
    __tablename__ = 'answers'

    id = Column('id', UUID(as_uuid=True), primary_key=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey('questions.id'), nullable=False)
    text = Column(TEXT, nullable=False)
    is_correct = Column(BOOLEAN, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    question = relationship("Question", back_populates="answers")

    def __init__(self, question_id: UUID, text: str, is_correct: bool) -> None:
        """
        Initialize Answer model
        :param question_id: UUID
        :param text: str
        :param is_correct: bool
        """
        self.id = uuid.uuid4()  # pylint: disable=invalid-name
        self.question_id = question_id
        self.text = text
        self.is_correct = is_correct

    def __repr__(self) -> str:
        """
        Answer model representation
        :return: str
        """
        return (f"<Answer(id={self.id}, "
                f"question_id={self.question_id}, "
                f"text={self.text}, "
                f"is_correct={self.is_correct})>"
                )
