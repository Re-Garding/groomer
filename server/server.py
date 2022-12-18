"""Server for Grooming Project"""

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from jinja2 import StrictUndefined
import os, model, crud

app = Flask(__name__)