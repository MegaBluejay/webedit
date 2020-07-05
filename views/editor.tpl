<!DOCTYPE html>
<html lang="en">
    <head>
        <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">
        <style>
            #editor {
                width: 99vw;
                height: 85vh;
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
        <a href="/logout">logout</a>
        <script src="/js/bootstrap.min.js"></script>
    </body>
</html>