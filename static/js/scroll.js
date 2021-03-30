$(window).scroll(function(){
    var s = $(window).scrollTop();

    if(s<360){
        $('.fab').css('color', 'white');
    } else if(s<1170){
        $('.fab').css('color', 'black');
    } else{
        $('.fab').css('color', 'gray');
    }
});