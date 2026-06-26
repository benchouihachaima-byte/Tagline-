from flask import Flask, render_template

app = Flask(__name__)

# قاعدة البيانات (المستويات -> الشعب -> المواد)
DATA = {
    "أولى ثانوي": {
        "جذع مشترك": [ "الرياضيات" , "العلوم الفيزيائية", "علوم الطبيعة والحياة" ]
    },
    "ثانية ثانوي": {
        "رياضيات": [ "الرياضيات" , "العلوم الفيزيائية", "علوم الطبيعة والحياة"],
        "علوم تجريبية": [ "الرياضيات" , "العلوم الفيزيائية", "علوم الطبيعة والحياة"]
    },
    "ثالثة ثانوي": {
        "رياضيات": ["الرياضيات" , "العلوم الفيزيائية", "علوم الطبيعة والحياة" , "الفلسفة", "اللغة العربية", "اللغة الفرنسية", "اللغة الإنجليزية", "التاريخ والجغرافيا", "التربية الإسلامية"],
        "علوم تجريبية": ["الرياضيات" , "العلوم الفيزيائية", "علوم الطبيعة والحياة" , "الفلسفة", "اللغة العربية", "اللغة الفرنسية", "اللغة الإنجليزية", "التاريخ والجغرافيا", "التربية الإسلامية"]
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
    return render_template('subjects.html', level=level, stream=stream, subjects=DATA[level][stream])

# سنضيف صفحة المحاور لاحقاً عند تحديدها
@app.route('/chapters/<level>/<stream>/<subject>')
def chapters(level, stream, subject):
    return f"صفحة محاور {subject} للمستوى {level} ستضاف هنا قريباً!"

if __name__ == '__main__':
    app.run(debug=True)