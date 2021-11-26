from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import request

bp = Blueprint("site", __name__)


@bp.route('/')
def home():
   return render_template("main.html")