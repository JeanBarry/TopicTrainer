from dotenv import load_dotenv
from src.app import create_app
from src.constants import app_env, production

load_dotenv()

app = create_app()

if app_env != production:
    app.run(debug=True, host='0.0.0.0')

application = app
