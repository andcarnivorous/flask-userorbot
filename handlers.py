from app import app
from flask import request, render_template

@app.errorhandler(412)
def invalid_keys():
    return "The provided json KEYS are invalid",412

@app.errorhandler(412)
def invalid_values():
    return "The provided json VALUES are invalid",412
