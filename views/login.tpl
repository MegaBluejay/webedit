<!DOCTYPE html>
<html lang="en">
    <head>
        <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">
        <style>
            #loginform {
                display: flex;
                height: 30px;
            }
            input[type=password] {
                width: 100%;
            }
        </style>
    </head>
    <body>
        <div class="row-fluid">
            <div class="span4 offset4">
                <form action="/login" method="post" id="loginform">
                    <input type="password" name="password" placeholder="password" />
                    <button type="submit">Login</button>
                </form>
            </div>
        </div>
        <script src="/js/bootstrap.min.js"></script>
    </body>
</html>