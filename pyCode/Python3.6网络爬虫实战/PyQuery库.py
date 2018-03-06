#coding=utf-8
from pyquery import PyQuery
content='''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=0.4, maximum-scale=0.4, user-scalable=no" />
	<meta name="msapplication-tap-highlight" content="no" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" />
    <!--    <link rel="apple-touch-icon-precomposed" href="images/touch-icon-ipad-retina.png?v=1" />-->
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="robots" content="noarchive" />
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
	<meta name="renderer" content="webkit" />
	<title>表单 | 麦客CRM</title>
    <!--[if lte IE 8]>
    <script src="js/libs/respond.min.js"></script>
    <![endif]-->
	<link rel="stylesheet" href="css/mgGlobal.css?v=180223"/>
    <link rel="stylesheet" href="css/cpDropDown.css?v=180126"/>
    <link rel="stylesheet" href="css/cpCalendar.css?v=180202"/>
	<link rel="stylesheet" href="css/cpRichTextEditor.css?v=1709213"/>
    <link rel="stylesheet" href="css/popwin.css?v=180226"/>
    <link rel="stylesheet" href="css/mgImageEditor.css?v=171020"/>
    <link rel="stylesheet" href="css/contactTagSelect.css?v=180223"/>
	<link rel="stylesheet" href="css/inputStructured.css?v=170315"/>
    <link rel="stylesheet" href="css/header.css?v=1803022"/>
	<link rel="stylesheet" href="css/headerBuilder.css?v=180223"/>
    <link rel="stylesheet" href="css/form.css?v=170810"/>
    <link rel="stylesheet" href="css/formList.css?v=180223"/>
    <link rel="stylesheet" href="css/formCreate.css?v=180305"/>
    <link rel="stylesheet" href="css/cpEditorDrag.css?v=170629"/>
    <link rel="stylesheet" href="css/formBuilder.css?v=1802232"/>
    <link rel="stylesheet" href="css/formStyle.css?v=180301"/>
    <link rel="stylesheet" href="css/formBuilderComponentSettings.css?v=180223"/>
    <link rel="stylesheet" href="css/formFeedback.css?v=1802232"/>
    <link rel="stylesheet" href="css/formOrder.css?v=171123"/>
    <link rel="stylesheet" href="css/formSettlement.css?v=180223"/>
    <link rel="stylesheet" href="css/formUnexpectedCheckIn.css?v=170909"/>
    <link rel="stylesheet" href="css/ticketValidation.css?v=1709213"/>
	
    <link rel="stylesheet" href="css/font.css?v=170810" media="none" onload="if(media!='all')media='all'">
	
    <!--[if lt IE 9]>
    <script type="text/javascript" src="js/libs/html5.js"></script>
    <script src="js/libs/excanvas.js" charset="UTF-8"></script>
    <![endif]-->
    	<link rel="apple-touch-icon" sizes="57x57" href="/images/favicon/apple-touch-icon-57x57.png">
	<link rel="apple-touch-icon" sizes="60x60" href="/images/favicon/apple-touch-icon-60x60.png">
	<link rel="apple-touch-icon" sizes="76x76" href="/images/favicon/apple-touch-icon-76x76.png">
	<link rel="apple-touch-icon" sizes="72x72" href="/images/favicon/apple-touch-icon-72x72.png">
	<link rel="apple-touch-icon" sizes="114x114" href="/images/favicon/apple-touch-icon-114x114.png">
	<link rel="apple-touch-icon" sizes="120x120" href="/images/favicon/apple-touch-icon-120x120.png">
	<link rel="apple-touch-icon" sizes="144x144" href="/images/favicon/apple-touch-icon-144x144.png">
	<link rel="apple-touch-icon" sizes="152x152" href="/images/favicon/apple-touch-icon-152x152.png">
	<link rel="apple-touch-icon" sizes="180x180" href="/images/favicon/apple-touch-icon-180x180.png">
	<link rel="icon" type="image/png" href="/images/favicon/favicon-32x32.png" sizes="32x32">
	<link rel="icon" type="image/png" href="/images/favicon/favicon-194x194.png" sizes="194x194">
	<link rel="icon" type="image/png" href="/images/favicon/favicon-96x96.png" sizes="96x96">
	<link rel="icon" type="image/png" href="/images/favicon/android-chrome-192x192.png" sizes="192x192">
	<link rel="icon" type="image/png" href="/images/favicon/favicon-16x16.png" sizes="16x16">
	<link rel="manifest" href="/images/favicon/manifest.json">
	<meta name="msapplication-TileColor" content="#2d89ef">
	<meta name="msapplication-TileImage" content="/images/favicon/mstile-144x144.png">
	<meta name="theme-color" content="#267DC5"></head>

<!--[if IE 8]> <body class="ie8 cn win sld_cn"> <![endif]-->
<!--[if IE 9]> <body class="ie9 cn win sld_cn"> <![endif]-->
<!--[if gt IE 9]> <body class="cn win sld_cn"> <![endif]-->
<!--[if !IE]>--><body class="cn win sld_cn"><!--<![endif]-->

<script type="text/javascript">
	var sld = 'cn',
		clSld = 'vickywang',
		clFlgExt = null,
		uId = 762937,
		uAuthority = 1,
		uAccount = '769609120@qq.com',
		uName = '露露',
		uAvatarUri = '/images/avatar/avatar_m7.png',
		uOrgName = '上海信隆行',
		uMobile = '769609120@qq.com',
		uFlgUg0 = 34,
		_U = 'ugc_2_a/pub/f5/f5089e229a4b91f9820c2ecc25a8c419/form/image/';
</script>
<!-- <div id="header">
	<a class="h_label img contact"></a>
	<a class="h_label img group"></a>
	<a class="h_label img form"></a>
	<a class="h_label img email"></a>

	<div class="h_user">
		<a class="u_setting"></a>
		<ul class="u_opeList">

		</ul>
	</div>
	<div class="cp_palaceHolder h_quickSearch">
		<span class="cp_ph_span qs_tip">搜索联系人、群组</span>
		<input class="cp_ph_input" id="quickSearch" />
		<span class="btn_quickSearch"></span>
	</div>
</div> --><div class="wrapper">
</div>
<!--功能弹窗层-->
<div class="popfunc" id="popfunc"></div>
<div class="popfuncTopper" id="popfuncTopper"></div>
<div class="popAvatarUpload" id="popAvatarUpload"></div>
<!--付款弹窗-->
<div class="popPay" id="popPay"></div>
<!--全局的錯誤提示-->
<div class="popwin" id="popwin"></div>
<script type="text/javascript" src="./js/commons.js?v=171218"></script>
<script type="text/javascript" src="./js/common-cn.js?v=1803052"></script>
<script type="text/javascript" src="./form/js/common-cn.js?v=180223"></script>
<script type="text/javascript" src="./js/bundle.js?v=180306"></script>
<script type="text/javascript" src="./js/app.js?v=180306"></script>
<script type="text/javascript" charset="UTF-8">
    (function(){
        document.write('<script src="//api.map.baidu.com/api?v=2.0&ak=EDb798da5e9a45ddd62246439064d449"  type="text/javascript"'+'><'+'/script>');
    })();
    MK.Form();
</script>
<script type="text/javascript">
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-44048469-1', 'auto');
  ga('send', 'pageview');
</script>
</body>
</html>
'''
document1=PyQuery(url='http://www.baidu.com')
document2=PyQuery(content)
#document3=PyQuery(filename='test.html')
print(document1('link'))
print(document2('link'))