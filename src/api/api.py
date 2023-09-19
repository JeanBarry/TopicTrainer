from flask_restx import Api, Resource, Namespace
from src.api.models.topic import topic_output_schema
from src.controllers import TopicController


def create_api(app):
    """
    Create a Flask Restx API using the app factory pattern.
    :param app: Flask app
    :return: None
    """

    api = Api(
        app,
        title='Topic Trainer API',
        description='API to manage topics, questions and answers ',
        doc='/api/doc/',
        version='0.1a'
    )

    app.config['RESTX_MASK_SWAGGER'] = False

    topic_namespace = Namespace('topic', description='Topic related operations', path='/api/topic')
    topic_model = api.model('Topic', topic_output_schema)

    class Topic(Resource):
        """
        Topic resource methods
        """
        @api.doc(id='get_topics',
                 description='Get all topics',
                 responses={200: 'Success', 400: 'Bad Request'})
        @api.marshal_with(topic_model)
        def get(self):
            """
            Read operation for topic resource
            Gets all topics
            :return: List of topics
            """
            topic_controller = TopicController()
            response = topic_controller.get_all_topics()
            return response, 200

    topic_namespace.add_resource(Topic, '/')
    api.add_namespace(topic_namespace)
