(function(){
    var content_data;

    function loadNext($el) {
        var me = $el;
        me.children().first().remove();
        me.addClass('fade');

        $.get('/', {life_img: life_img}, function(data, status, xhr) {
            content_data = data;
        });

        setTimeout(function(){
            if(typeof content_data !== 'undefined'){
                life_img = content_data.life_img;
                $('.img_layer').attr('style', 'background: url(' + life_img + ') no-repeat center center; background-size: cover;');
                $('#pattern').attr('style', content_data.pattern_style);
                me.removeClass('fade');
            }
        }, 5000, this);
    }

    setInterval(function(){ loadNext($('.msg_layer')); }, 10000);
})();

