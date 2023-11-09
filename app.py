from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        try:
            increment = int(request.form['increment'])
            session['counter'] = session.get('counter', 0) + increment
        except ValueError:
            error = "Error: Invalid input."
        return redirect(url_for('index'))
    return render_template('index.html', counter=session.get('counter', 0), error=error)

if __name__ == '__main__':
    app.secret_key = 'super-secret-key'
    app.run(debug=True)