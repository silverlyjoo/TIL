# CRUD PROJECT



190208 | CRUD 프로젝트



워크스페이스 생성 방법

```
# install pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
pyenv rehash


# install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc


# etc
python -V
pip install -U pip
pip install flask
pip install requests
pip freeze > req.txt
```



```
$ pip install flask_sqlalchemy
$ pip install flask_migrate

$ flask db init
$ flask db migrate
$ flask db upgrade

```





```python
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
# 만든 클래스명

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db에 app 연동
db.init_app(app)

# migrate 초기화
migrate = Migrate(app, db)

##
##


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

```python
# 파이썬 models.py

from flask_sqlalchemy import SQLAlchemy

#sqlalchemy 초기화
db = SQLAlchemy()

# sqlalchemy datatype
# Integer / String(size) / Text / DateTime / Float / Boolean

class User(db.model):
    
    __tablename__ = 'users'
    id = db.column(db.Integer, primary_key=True)
    nickname = db.column(db.String(20), nullable=False)
    address = db.column(db.String(20), nullable=False)
```





```python
# app.py 내용

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users) # templates 폴더 만들기



# @app.route('/users/create') # unique 한 페이지 url

@app.route('/users/create/') # 후방 슬래쉬 없이 엑세스 가능
def create():
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    user = User(nickname=nickname, address=address)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/delete/<int:id>/')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/edit/<int:id>/')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
    
@app.route('/users/update/<int:id>/')
def update(id):
    user = User.query.get(id)
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    user.nickname = nickname
    user.address = address
    db.session.commit()
    return redirect(url_for('index'))
```

