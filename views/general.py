# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

mod = Blueprint("general", __name__)

@mod.route('')
def index():
    """Render index page"""
    return render_template("index.html")
