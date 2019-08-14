from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import os, requests, datetime, csv






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

# 영화목록출력
@app.route('/movie')
def movies():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '하울의움직이는성']
    return render_template('movie.html', movies=movies)
    
# fake google

@app.route('/google')
def google():
    return render_template('google.html')

# 세제곱
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다'
    
# 핑퐁

@app.route('/ping')
def ping():
    pong_name = request.args.get('pong_name')
    return render_template('ping.html', pong_name = pong_name)

@app.route('/pong')
def pong():
    msg = request.args.get('msg')
    ping_name = request.args.get('ping_name')
    return render_template('pong.html', ping_name = ping_name, msg=msg)
    
    
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')

@app.route('/pong_new', methods=['POST'])
def pong_new():
    new_ping = request.form.get('new_ping')
    new_msg = request.form.get('new_msg')
    return render_template('pong_new.html', ping_new_name = new_ping, msg = new_msg)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    req = requests.get(url+username).text
    soup = BeautifulSoup(req, 'html.parser')
    rank = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')

    return render_template('opgg_result.html', username=username, rank = rank.text, wins = wins.text, loses=loses.text)


@app.route('/timeline')
def timeline():
    with open('timeline.csv', newline='', encoding='utf-8') as csvfile:
        readers = csv.DictReader(csvfile)
        data = [(row['username'], row['message']) for row in readers]
    return render_template('timeline.html', data=data)
    
    

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username': username, 'message': message})
    return redirect('/timeline')
    # return render_template('timeline_create.html', username=username, message=message)




    
if __name__ == '__main__':
   app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)