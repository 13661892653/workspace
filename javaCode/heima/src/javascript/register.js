/* window.onload = function () {
	     //获取指定id的标签元素
	     var user = document.getElementById("userid");
	     //获取指定id的标签元素的值
	     var username = user.value;
	     alert(username);
	 };*/

function checkForm() {
    //alert("绑定成功");
    //获取用户输入的数据
    var user = document.getElementById("userid").value;
    //校验用户名不能为空
    if (user == "") {
        alert("用户名不能为空");
        return false;
    }

    var password = document.getElementById("pid1").value;
    if (password == "") {
        alert("密码不能为空");
        return false;
    }

    //校验两次密码输入是否相同
    var repassword = document.getElementById("pid2").value;
    if (password != repassword) {
        alert("两次密码输入不一致");
        return false;
    }

    //邮箱校验,正则表达式注意加上双引号
    var emailV = document.getElementById("emailid");
    if (!"/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+.([a-zA-Z0-9_-])+/"
        .test(emailV)) {
        alert("邮箱地址不合法");
        return false;
    }

}