from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Load job entries from JSON
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            try:
                jobs = json.load(file)
            except json.JSONDecodeError:
                jobs = []
    else:
        jobs = []

    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['POST'])
def add_job():
    job = {
        'company': request.form['company'],
        'title': request.form['title'],
        'link': request.form['link'],
        'notes': request.form['notes']
    }

    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(job)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
