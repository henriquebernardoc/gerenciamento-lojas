
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

promocoes_blueprint = Blueprint('promocoes', __name__)

@promocoes_blueprint.route("/promocoes")
def promocoes():
  return render_template("dashboard.html")
