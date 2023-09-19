from flask_restx import fields

topic_output_schema = {
    'id': fields.String(required=True, description='Topic id'),
    'technology': fields.String(required=True, description='Technology name', max_length=255),
    'name': fields.String(required=True, description='Topic name', max_length=255),
    'description': fields.String(required=True, description='Topic description', max_length=255),
    'difficulty': fields.String(required=True, description='Topic difficulty',
                                enum=['easy', 'medium', 'hard']),
    'logoUrl': fields.String(attribute='logo_url', required=True,
                             description='Topic logo url', max_length=255),
}
