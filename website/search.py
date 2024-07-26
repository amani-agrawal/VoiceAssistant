from flask import Blueprint, render_template, request, flash, jsonify
import subprocess

search = Blueprint('search', __name__)


@search.route('/')
def home():
    return render_template("search.html")

@search.route('/run-script', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(['python', './website/processing.py'], capture_output=True, text=True)
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})