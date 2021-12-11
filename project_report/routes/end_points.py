from flask import render_template
from project_report import app, data
@app.route('/')
def index():
    return render_template('index.html', columns = data.columns, values = data.values.tolist())

    