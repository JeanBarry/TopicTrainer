import os

app_env = os.getenv('ENV')

environments = {
    'production': 'production',
    'development': 'development',
}

production = environments.get('production')
