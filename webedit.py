from bottle import run, get,post,request,template,redirect,static_file
from bottle import app as make_app
from pathlib import Path
from os import linesep
from cork import Cork
from beaker.middleware import SessionMiddleware

file_path = './test'

session_opts = {
    'session.cookie_expires': False,
    'session.encrypt_key':'bpvSpCLaswxnSwmCifsEnnWIGXtqTiaUWhjIIkrNeplDqsaBIF',
    'session.httponly': True,
    'session.type': 'cookie',
    'session.validate_key': True
}

cork = Cork('authconf')
auth = cork.make_auth_decorator(fail_redirect='/login',role='admin')
app = SessionMiddleware(make_app(),session_opts)

file = Path(file_path)
file.touch()
with file.open(newline='') as f:
    text = f.read()
    filesep = ([sep for sep in ['\r\n','\r','\n'] if sep in text]+[linesep])[0]

@get('/login')
def login_form():
    return template('login')

@post('/login')
def login():
    password = request.forms.password
    cork.login('admin',password, success_redirect='/',fail_redirect='/login')

@get('/logout')
def logout():
    cork.logout(success_redirect='/login')

@get('/')
@auth()
def editor():
    with file.open('r') as f:
        text = f.read()
    lines = min(50,len(text.split('\n')))
    return template('editor', text=text, lines=lines)

@post('/')
def edit():
    text = request.forms.editor.replace('\r\n',filesep)
    with file.open('w') as f:
        f.write(text)
    redirect('/')

@get('/images/<filename:re:.*\.png>')
def image(filename):
    return static_file(filename,root='./res/img', mimetype='image/png')

@get('/js/<filename:re:.*\.js>')
def script(filename):
    return static_file(filename, root='./res/js')

@get('/css/<filename:re:.*\.css>')
def style(filename):
    return static_file(filename,root='./res/css')


if __name__ == '__main__':
    run(app=app,port=8080)
