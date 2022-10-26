from app import app
from flask import jsonify, render_template, request
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    with open('data.txt', 'r') as f:
        data=f.read()
    
    userHeader = data
    return render_template('index.html', userHeader=userHeader)

@app.route('/api/cep/<cep>')
def cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    req = requests.get(url).json()
    with open('data.txt', 'r') as f:
        data=f.read()
    
    return req

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        db = {
            "user": user,
            "passw": passwd
        }
        
        f = open('data.txt', 'w')
        data=f.write(db['user'])
        f.close()
        
        f2 = open('password.txt', 'w')
        data=f2.write(db['passw'])
        f2.close()
        
        msg = '{}, {}'.format(user, passwd)
        return render_template('admin.html', msg=msg)
    
    return render_template('admin.html')
    
    
    