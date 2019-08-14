from flask import Flask, render_template
import os
import datetime



app = Flask(__name__)


@app.route('/')
def index():
    return 'hello there! kk'
    
    
# 5월 20일부터 d-day 카운트 출력

@app.route('/d_day')
def d_day():
    dday = datetime.datetime(2019,5,20) - datetime.datetime.now()
    help = dday.days
    return f'휴가까지 {help}일 남았습니다!!'
    
# variable routing
@app.route('/greeting/<string:name>')
def greeting(name):
    # greeting.html 로 위처럼 안녕 누구누구를 출력해 보세요.
    return render_template('greeting.html', html_name=name)
    
@app.route('/movie')
def movies():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '하울의움직이는성']
    return render_template('movie.html', movies=movies)
    
    
    # return f'안녕, {name}'
    
    
    
    
    
    

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다'
    
    





    
if __name__ == '__main__':
   app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)