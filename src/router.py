from flask import make_response, jsonify, request, send_from_directory


def router(app):
    """
    Register routes for the Flask app.

    :param app: Flask app
    :return: None
    """

    @app.route('/logos/<path:path>', methods=['GET'])
    def logos(path):
        if request.method != 'GET':
            return make_response(jsonify({'message': 'Method not allowed!'}), 405)
        return send_from_directory('assets/logos', path)
