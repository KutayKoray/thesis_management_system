from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_thesis.html')
def add_thesis():
    return render_template('add_thesis.html')

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/thesis_detail.html')
def thesis_detail():
    return render_template('thesis_detail.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8800)
