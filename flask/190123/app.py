from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕하세요!!!'


# @app.route('/html')
# def html():
#     return render_template('chicken.html')


# chicken.html 페이지를 띄워주세요







@app.route('/html_name/<string:name>')
def html_name(name):
    return render_template('chicken.html', yourname=name)

@app.route('/dictionary/<string:word>')
def my_dict(word):
    my_words = {'apple' : '사과', 'banana' : '바나나'}
    return render_template('word.html', word=word, my_words=my_words)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)