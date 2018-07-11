<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>信隆行CRM系统</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <meta content="" name="description"/>
    <meta content="" name="author"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link href="/dist/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/simple-line-icons.min.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/uniform.default.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/lock.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/components.css" id="style_components" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/plugins.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/layout.css" rel="stylesheet" type="text/css"/>
    <link href="/dist/css/darkblue.css" rel="stylesheet" type="text/css" id="style_color"/>
    <link href="/dist/css/custom.css" rel="stylesheet" type="text/css"/>

</head>
<body>
<div class="page-lock">
    <div class="page-logo">
        <img src="/img/logo_home.png" alt=""/>
    </div>
    <div class="page-body">
        <div class="lock-head">
            CRM系统
        </div>
        <div class="lock-body">
            <div class="pull-left lock-avatar-block">
                <img src="/img/photo3.jpg" class="lock-avatar">
            </div>
            <form class="lock-form pull-left" action="/login" method="post">
                <div class="form-group">
                    <input name="memberPhone" id="username" size="25" class="form-control placeholder-no-fix" type="text" autocomplete="off" placeholder="用户名" />
                </div>
                <div class="form-group">
                    <input name="memberPwd" id="password" size="25" class="form-control placeholder-no-fix" type="password" autocomplete="off" placeholder="密码" />
                </div>
                <div class="form-actions">
                    <button type="submit" class="btn btn-success uppercase">登录</button>
                </div>
            </form>
        </div>
        <div class="lock-bottom">
        <#if msg??><label style="color: #ff0007"> ${msg}</label></#if>
            <a href=""></a>
        </div>
    </div>
    <div class="page-footer-custom">
        2017 &copy; 上海信隆行信息科技股份有限公司
    </div>
</div>
<script src="/dist/js/jquery-1.10.2.min.js" type="text/javascript"></script>
<script src="/dist/js/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>
<script src="/dist/js/jquery.blockui.min.js" type="text/javascript"></script>
<script src="/dist/js/jquery.cokie.min.js" type="text/javascript"></script>
<script src="/dist/js/jquery.uniform.min.js" type="text/javascript"></script>
<script src="/dist/js/jquery.backstretch.min.js" type="text/javascript"></script>
<script src="/dist/js/metronic.js" type="text/javascript"></script>
<script src="/dist/js/demo.js" type="text/javascript"></script>
<script src="/dist/js/layout.js" type="text/javascript"></script>
<script>
    jQuery(document).ready(function() {
        //Metronic.init(); // init metronic core components
        //Layout.init(); // init current layout
        //Demo.init();
    });
</script>
</body>
</html>