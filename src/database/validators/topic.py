from cerberus import Validator

schema = {
    'technology': {
        'type': 'string',
    },
    'name': {
        'type': 'string',
    },
    'description': {
        'type': 'string',
    },
    'difficulty': {
        'type': 'string',
        'allowed': ['EASY', 'MEDIUM', 'HARD'],
    },
}

creation_schema = {
    key: {**value, 'required': True, 'empty': False}
    for key, value in schema.items()
}

topic_validator = Validator(schema)
topic_creation_validator = Validator(creation_schema)


def validate_topic_creation(topic: dict) -> bool:
    """
    Validate topic creation
    :param topic: Topic dict with all the required attributes

    :return: bool representing if the topic is valid
    """
    return topic_creation_validator.validate(topic)
