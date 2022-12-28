import os
from app import create_app
from flask_jwt_extended import JWTManager

setting_module = os.getenv('APP_SETTINGS_MODULE')
if not setting_module:
    setting_module = os.environ.get('APP_SETTINGS_MODULE', 'config.development')

app = create_app(setting_module)
jwt = JWTManager(app)

@app.route('/input_test', methods=['GET'])
def input_test():
    return 'OK'

