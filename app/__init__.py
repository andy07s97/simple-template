# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # 把 routes 分出去管理
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
