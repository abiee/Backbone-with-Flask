# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

app = Blueprint("general", __name__)

@app.route('/')
def index():
    """Render index page"""
    return render_template("index.html")
