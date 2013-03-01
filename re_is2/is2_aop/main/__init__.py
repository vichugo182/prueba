from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    if 'login' in session:
        return render_template('login.html')
    login=request.cookies.get('login')
    if(login==True):
        return render_template('menu.html',name=login)
    return render_template('login.html')
    

@app.route('/login',methods=['GET', 'POST'])   
def login():
    #session['login']='true'
    if request.method == 'POST':
        #session['login'] ='true'
        return redirect(url_for('menu'))
    
    return redirect(url_for('menu'))

@app.route('/menu')   
def menu():
    return render_template('menu.html',name='AOP')


@app.route('/base')   
def base():
    return render_template('child.html',title='AOP')

if __name__ == '__main__':
    app.run()