from cerberus import Validator

schema = {
    'question_id': {
        'type': 'string',
    },
    'text': {
        'type': 'string',
    },
    'is_correct': {
        'type': 'boolean',
    },
}

creation_schema = {
    key: {**value, 'required': True, 'empty': False}
    for key, value in schema.items()
}

answer_validator = Validator(schema)
answer_creation_validator = Validator(creation_schema)


def validate_answer_creation(answer: dict) -> bool:
    """
    Validate answer creation
    :param answer: Answer dict with all the required attributes

    :return: bool representing if the answer is valid
    """
    return answer_creation_validator.validate(answer)
