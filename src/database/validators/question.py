from cerberus import Validator

schema = {
    'topic_id': {
        'type': 'string',
    },
    'text': {
        'type': 'string',
    },
}

creation_schema = {
    key: {**value, 'required': True, 'empty': False}
    for key, value in schema.items()
}

question_validator = Validator(schema)
question_creation_validator = Validator(creation_schema)


def validate_question_creation(question) -> bool:
    """
    Validate question creation
    :param question: Question dict with all the required attributes

    :return: bool representing if the question is valid
    """
    return question_creation_validator.validate(question)
