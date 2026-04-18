# from db import db, Decision
# from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request

# from .views import


decision_app = Blueprint("decision", __name__, template_folder="./templates")
