/**
 * Created by colby on 8/28.
 */

//跑马灯案例
function test(){
    var tag=document.getElementById('id1');
    var content=tag.innerText;
    var f=content.charAt(0);
    var l=content.substring(1,content.length);
    var new_str=l+f;
    tag.innerText=new_str;
}
setInterval('test()',500)
