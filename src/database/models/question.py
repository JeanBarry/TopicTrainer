# pylint: disable=not-callable, too-few-public-methods
import uuid
from sqlalchemy import Column, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT
from src.database.models.common import Base


class Question(Base):
    """
    Question model
    Used to store questions
    """
    __tablename__ = 'questions'

    id = Column(UUID(as_uuid=True), primary_key=True)
    topic_id = Column(UUID(as_uuid=True), ForeignKey('topics.id'), nullable=False)
    text = Column(TEXT, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    topic = relationship("Topic", back_populates="questions")
    answers = relationship("Answer", back_populates="question")

    def __init__(self, topic_id: UUID, text: str) -> None:
        """
        Initialize Question model
        :param topic_id: UUID
        :param text: str
        """
        self.id = uuid.uuid4()  # pylint: disable=invalid-name
        self.topic_id = topic_id
        self.text = text

    def __repr__(self) -> str:
        """
        Question model representation
        :return: str
        """
        return f"<Question(id={self.id}, topic_id={self.topic_id}, text={self.text})>"
