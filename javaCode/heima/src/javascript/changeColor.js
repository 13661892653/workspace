/**
 * colby 2018-08-02
 */
function changeColor(){
    //var tbodyV=document.getElementById(table1id).getElementsByTagName('tbody');
    //获取表格的第一个tbody标签
    var tbodyV=document.getElementById("table1id").tBodies[0];
    //获取tbody的总行数rows
    var rowNum=tbodyV.rows.length;
    //遍历下标，跟2取余，注意0是第一行
    for(var i=0;i<rowNum;i++){
        if((i % 2)==0){
            //奇数行为红色
            tbodyV.rows[i].style.background="red";
        }else{
            //偶数行为黑色
            tbodyV.rows[i].style.background="gold";
        }
    }
}