$(function(){
    $('.query').click(function(){
    console.log('触发点击');
    $.ajax({
        url: '/app/',
			type: 'POST',
			data: {},
            dataType:'json',
            traditional:true,
			success: function(ret){
				// data是服务器端返回的字符串
                console.log('返回成功');
                $('#tbody').empty();
                $.each('ret',function (i,item) {
                    console.log(item);
                    var vfields = item.fields;
                    $("#tbody").append(
                        "<tr id="+vfields.id+">"
                        +"<td>"+1+"</td>"
                        +"<td>"+vfields.name+"</td>"
                        +"<td>"+vfields.r_host_app.name+"</td>"
                        +"<td>"
                            +"<input type='button' class='edit'    value='编辑'></input>"
                            +"<input type='button' class='detail'  value='详细'></input>"
                            +"<input type='button' class='delete'  value='删除'></input>"
                        +"</td>"
                        +"</tr>"
                    );
                });
		}
    });
});

    $('.btn-add').click(function(){
        $('.shade,.add-list').removeClass('hide');
    });

    $('.glyphicon-remove').click(function(){
        $('.shade,.add-list').addClass('hide');
    });
});
