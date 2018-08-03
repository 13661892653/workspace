function provinceCityChange() {
    var proid = document.getElementById("proid");
    for (var i = 0; i < provinceArr.length; i++) {
        var textNode = document.createTextNode(provinceArr[i][0]);
        //创建一个option元素节点
        var optionE = document.createElement("option");
        //将文本节点添加到li元素节点
        optionE.appendChild(textNode);
        //再讲li节点添加到ul节点最后
        proid.appendChild(optionE);
    }
}

function getCity() {
    var tag = document.getElementById("proid");
    var index = tag.selectedIndex;
    var proName = tag.options[index].text; // 选中文本
    console.log(proName);
    for (var i = 0; i < cityArr.length; i++) {
        if (proName == cityArr[i][0]) {
            console.log(cityArr[i][0]);
            var cityid = document.getElementById("cityId");
            initCity(cityid);
            for (var j = 1; j < cityArr[i].length; j++) {
                console.log(cityArr[i][j]);
                /*console.log(cityArr[i][j]);
                var textNode=document.createTextNode(cityArr[i][j]);
                //创建一个option元素节点
                var optionE=document.createElement("option");
                //将文本节点添加到li元素节点
                optionE.appendChild(textNode);
                //再讲li节点添加到ul节点最后
                cityid.appendChild(optionE);*/
                var textNode2 = document.createTextNode(cityArr[i][j]);
                var optionE2 = document.createElement("option");
                optionE2.appendChild(textNode2);
                cityid.appendChild(optionE2)
            }
        }
    }
}

function initCity(cityid) {
    //清空城市列表，保留第一个元素
    cityid.options.length = 1;
}