from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sum')
def sum_page():
    a = 5
    b = 7
    return render_template('sum.html', a=a, b=b)


if __name__ == '__main__':
    app.run(debug=True)
