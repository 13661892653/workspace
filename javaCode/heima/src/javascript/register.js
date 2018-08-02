/* window.onload = function () {
	     //获取指定id的标签元素
	     var user = document.getElementById("userid");
	     //获取指定id的标签元素的值
	     var username = user.value;
	     alert(username);
	 };*/

/*
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
}*/
function showTips(id, message) {
    //光标聚焦到文本框的时候
    var checkValue = document.getElementById(id).value;
    va1 = document.getElementById("pid1").value;
    va2 = document.getElementById("pid2").value;
    if (checkValue != "") {
        //不为空就将提示信息清空
        document.getElementById(id + "span").innerHTML = "";
    } else {
        //为空的话给出提示信息
        document.getElementById(id + "span").innerHTML = "<font style='color: gray;' />" + message + "</font>";
    }
}

function check(id, message) {
    //光标离开文本框的时候
    var checkValue = document.getElementById(id).value;
    va1 = document.getElementById("pid1").value;
    va2 = document.getElementById(id).value;
    if (checkValue == "") {
        document.getElementById(id + "span").innerHTML = "<font style='color: red;' />" + message + "</font>";
    } else {
        //文本框不为空，且正在校验email的时候，校验email地址合法性
        if (id == "emailid") {
            if (!/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+.([a-zA-Z0-9_-])+/.test(checkValue)) {
                //alert(checkValue);
                message = "邮箱地址不合法！";
                document.getElementById(id + "span").innerHTML = "<font style='color: red;' />" + message + "</font>";
            }
        //文本框不为空，且正从校验密码框离开的时候，校验密码是否一致
        } else if (id == "pid2") {
            if (va1 != va2) {
                message = "密码不一致！";
                document.getElementById(id + "span").innerHTML = "<font style='color: red;' />" + message + "</font>";
            }
        } else {
            //除此之外，清空提示信息
            document.getElementById(id + "span").innerHTML = "";
        }
    }
}
