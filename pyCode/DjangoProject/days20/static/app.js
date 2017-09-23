function test(){
        console.log('ddddd');
            var appname=$('#appid').val();
            var hostname=$('#hostid').val();
            $.ajax({
                 url: '/app_ajax/',
                 data: {'appname':appname,'hostname':hostname},
                 type: 'POST',
                //默认traditional为false，设置为true时，传过去一个数组[]
                 traditional: true,
                 success: function(obj){
                             console.log(obj);
                         },
                         error: function () {
                             console.log('error');
                         }
                 });
        }
$(function(){
    $('.btn-add').click(function(){
        $('.shade,.add-list').removeClass('hide');
    });

    $('.glyphicon-remove').click(function(){
        $('.shade,.add-list').addClass('hide');
    });

    $('#btn_ajax_app').click(function () {
        console.log('ddddd');
            var appname=$('#appid').val();
            var hostname=$('#hostid').val();
            $.ajax({
                 url: '/app_ajax/',
                 data: {'appname':appname,'hostname':hostname},
                 type: 'POST',
                //默认traditional为false，设置为true时，传过去一个数组[]
                 traditional: true,
                 success: function(obj){
                             console.log(obj);
                         },
                         error: function () {
                             console.log('error');
                         }
                 });
    })
});


