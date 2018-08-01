/**
 * colby
 */

function init() {
    //设置显示广告图片的操作
    interval1 = setInterval("showAd()", 3000);
}

function showAd() {
    //设置style.display的属性为block，显示图片
    document.getElementById("imageid").style.display = "block";
    //清除显示图片的定时器
    window.clearInterval(interval1);
    //设置隐藏图片的定时操作
    interval2 = setInterval("clearAd()", 6000);
}

function clearAd() {
    //设置图片隐藏
    document.getElementById("imageid").style.display = "none";
    //清除隐藏图片的定时器
    window.clearInterval(interval2);
}