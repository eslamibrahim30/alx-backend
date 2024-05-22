#!/usr/bin/env python3
"""
This module for task 'Basic Flask app'
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    This function returns the root html file
    """
    return render_template('./templates/0-index.html')
