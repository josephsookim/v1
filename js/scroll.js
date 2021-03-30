$(window).scroll(function(){
    var s = $(window).scrollTop();
    
    console.log(s)

    if(s <360){
        $('.fab').css('color', 'white');
    } else{
        $('.fab').css('color', 'black');
    }
});