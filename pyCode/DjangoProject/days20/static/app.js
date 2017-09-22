function test(){
        console.log('ddddd');
            appname='dddddd';
            hostname=[1,2,3,4];
            $.ajax({
                 url: '/app_ajax/',
                 data: {'appname':appname,'hostname':hostname},
                 type: 'POST',
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
});


