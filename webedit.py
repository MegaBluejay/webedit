from bottle import run, get,post,request,template,redirect
from sys import argv
from pathlib import Path

file = Path(argv[1])

@get('/')
def editor():
    with file.open('r') as f:
        text = f.read()
    lines = len(text.split('\n'))
    return template('''
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <h1>Test</h1>
        <form action="/" method="post" id="editor">
            <input value="Save" type="submit" />
        </form>
        <br>
        <textarea name="area" id="area" wrap="hard" rows="{{lines}}" cols="80" form="editor">{{text}}</textarea>
    </body>
</html>    
''', text=text, lines=lines)

@post('/')
def edit():
    text = request.forms.area
    with file.open('w') as f:
        f.write(text)
    redirect('/')

run(host='localhost',port=8080,debug=True)