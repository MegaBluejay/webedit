<!DOCTYPE html>
<html>
    <head>
        <style>
            #editor {
                width: 100%;
                height: 100%;
                resize: none;
            }
            #submitbtn {
                border: none;
                background-color: white;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post" id="edform">
            <button type="submit" id="submitbtn"><img src="/images/save.png" /></button>
        </form>
        <textarea name="editor" id="editor" rows="{{lines}}" cols="100" wrap="off" form="edform">{{text}}</textarea>
    </body>
</html>