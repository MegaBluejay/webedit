<!DOCTYPE html>
<html lang="en">
    <head>
        <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">
        <style>
            html,body {
                height: 100%;
                width: 100%;
                margin: 0;
            }
            #editor {
                width: 99%;
                height: 85%;
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
        <textarea name="editor" id="editor" wrap="off" form="edform">{{text}}</textarea>
        <a href="/logout">logout</a>
        <script src="/js/bootstrap.min.js"></script>
    </body>
</html>