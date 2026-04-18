from flask import Blueprint, render_template, redirect, url_for, request


users_app = Blueprint("users", __name__, template_folder="./templates")
