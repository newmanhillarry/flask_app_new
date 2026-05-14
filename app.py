from flask import Flask, render_template, request, redirect, flash
import os


app = Flask(__name__)
app.secret_key = "zofa_secret_soccer_key" # Required for flash messages

# Add this line to find the correct folder path
basedir = os.path.abspath(os.path.dirname(__file__))
COMPLAINS_PATH = os.path.join(basedir, "complains.txt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/complains', methods=['GET', 'POST'])
def complains():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            # Use COMPLAINS_PATH instead of just "complains.txt"
            with open(COMPLAINS_PATH, "a") as f:
                f.write(message + "\n---\n")
            flash("Your complaint has been sent successfully!", "success")
        return redirect('/complains')
    return render_template('complains.html')

@app.route('/view-complains')
def view_complains():
    try:
        # Use COMPLAINS_PATH here too
        with open(COMPLAINS_PATH, "r") as f:
            content = f.read()
            complaints = [c.strip() for c in content.split('---') if c.strip()]
    except FileNotFoundError:
        complaints = []
    return render_template('view_complains.html', complaints=complaints)

if __name__ == '__main__':
    app.run(debug=True)