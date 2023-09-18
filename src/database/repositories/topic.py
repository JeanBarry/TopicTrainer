from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import SQLAlchemyError

from src.database import Database
from src.database.models import Topic
from src.database.validators import validate_topic_creation


class TopicRepository:
    """
    TopicRepository class to manage the operations of the Topic model.
    """

    def __init__(self):
        self.database = Database()

    def get_all(self) -> list[Topic]:
        """
        Get all topics.

        :return: The topics
        """
        session = self.database.get_session()
        topics = session.query(Topic).all()
        session.close()
        return topics

    def get_by_id(self, topic_id: UUID) -> Topic:
        """
        Get a topic by its id.

        :param topic_id: The resource id
        :return: The topic
        """
        session = self.database.get_session()
        topic = session.query(Topic).filter_by(id=topic_id).first()
        session.close()
        return topic

    def create(self, **kwargs) -> Topic or None:
        """
        Create a topic.

        :param kwargs: The topic attributes

        The topic attributes are:
            technology: The topic technology
            name: The topic name
            description: The topic description
            difficulty: The topic difficulty ("easy", "medium", "hard")

        :return: The created topic
        """

        if not validate_topic_creation(kwargs):
            print("Invalid topic attributes")
            return None

        topic = Topic(**kwargs)

        with self.database.get_session() as session:
            try:
                session.add(topic)
                session.commit()
                session.refresh(topic)
                return topic
            except SQLAlchemyError as exception:
                session.rollback()
                print(f"Error creating topic: {exception}")
                return None
