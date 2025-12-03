# app/routes.py
from flask import Blueprint

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return "This is Flask app"
