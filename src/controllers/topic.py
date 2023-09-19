# pylint: disable=too-few-public-methods
from src.database.models import Topic
from src.database.repositories import TopicRepository


class TopicUtils:
    """
    Utility class for Topic related operations
    """

    @staticmethod
    def build_logo_url(topic: dict) -> str or None:
        """
        Build logo url from topic technology
        :param topic: dict
        :return: str or None
        """
        topic_technology = topic.get('technology')
        topic_url = None
        if topic_technology:
            topic_url = f"/logos/{topic_technology.lower()}.svg"
        return topic_url

    @staticmethod
    def topic_adapter(topic: Topic) -> dict:
        """
        Adapter to modify topics to be sent to the client
        :param topic: Topic
        :return: dict
        """
        topic_dict = topic.to_dict()
        topic_dict.update({'logo_url': TopicUtils.build_logo_url(topic_dict)})
        return topic_dict


class TopicController:
    """
    Controller to manage the operations needed to
    interact with the Topic model and the client.
    """
    def __init__(self) -> None:
        self.topic_repository = TopicRepository()

    def get_all_topics(self) -> list[dict]:
        """
        Retrieve all topics in the client format
        :return: list[dict]
        """
        topics = self.topic_repository.get_all()
        response = [TopicUtils.topic_adapter(topic) for topic in topics]
        return response
