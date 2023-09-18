# pylint: disable=not-callable, too-few-public-methods
import uuid
from enum import Enum as PythonEnum
from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, ENUM
from src.database.models.common import Base

DIFFICULTY_ENUM_NAME = "difficulty_enum"


class DifficultyEnum(PythonEnum):
    """
    DifficultyEnum class
    Used to create ENUM type for difficulty
    """
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Topic(Base):
    """
    Topic model
    Used to store topics for questions
    """
    __tablename__ = "topics"

    id = Column(UUID(as_uuid=True), primary_key=True)
    technology = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(255), nullable=False)
    difficulty = Column(ENUM(DifficultyEnum, name=DIFFICULTY_ENUM_NAME), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    questions = relationship("Question", back_populates="topic")

    def __init__(self, technology: str, name: str, description: str, difficulty: str) -> None:
        """
        Initialize Topic model
        :param technology: str
        :param name: str
        :param description: str
        :param difficulty: str
        :return: None
        """
        self.id = uuid.uuid4()  # pylint: disable=invalid-name
        self.technology = technology
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def __repr__(self) -> str:
        """
        String representation of Topic model
        :return: str
        """
        return (f"<Topic(id={self.id}, "
                f"name={self.name}, "
                f"technology={self.technology}, "
                f"description={self.description}, "
                f"difficulty={self.difficulty}, "
                f"created_at={self.created_at}, "
                f"updated_at={self.updated_at})>"
                )

    def to_dict(self) -> dict:
        """
        Convert Topic model to dictionary
        :return: dict
        """
        return {
            "id": self.id,
            "technology": self.technology,
            "name": self.name,
            "description": self.description,
            "difficulty": self.difficulty.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
