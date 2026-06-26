from flask import Flask, render_template

app = Flask(__name__)

# قاعدة البيانات المحدثة
DATA = {
    "أولى ثانوي": {"جذع مشترك": {"رياضيات": {"الدوال": "500 دج"}, "فيزياء": {"المادة": "400 دج"}}},
    "ثانية ثانوي": {
        "رياضيات": {"رياضيات": {"المتتاليات": "600 دج"}, "فيزياء": {"الميكانيك": "500 دج"}},
        "علوم تجريبية": {"رياضيات": {"المتتاليات": "600 دج"}, "علوم": {"التركيب الضوئي": "500 دج"}}
    },
    "ثالثة ثانوي": {
        "رياضيات": {"رياضيات": {"الدوال الأسية": "800 دج"}},
        "علوم تجريبية": {"علوم": {"المناعة": "700 دج"}}
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/levels')
def levels():
    return render_template('levels.html', levels=list(DATA.keys()))

@app.route('/streams/<level>')
def streams(level):
    return render_template('streams.html', level=level, streams=list(DATA[level].keys()))

@app.route('/subjects/<level>/<stream>')
def subjects(level, stream):
    return render_template('subjects.html', level=level, stream=stream, subjects=list(DATA[level][stream].keys()))

@app.route('/chapters/<level>/<stream>/<subject>')
def chapters(level, stream, subject):
    return render_template('chapters.html', subject=subject, chapters=DATA[level][stream][subject])

if __name__ == '__main__':
    app.run(debug=True)