from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home(): return render_template('home.html')
@app.route('/levels')
def levels(): return render_template('levels.html')
@app.route('/subjects')
def subjects(): return render_template('subjects.html')
@app.route('/chapters')
def chapters(): return render_template('chapters.html')

if __name__ == '__main__': app.run()