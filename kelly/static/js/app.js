(function(){
    function clickNext(e) {
        e.preventDefault();
        e.target.setAttribute('class', 'fade');
        setTimeout(function(){
            console.log(e)
            window.location = e.target.getAttribute('href');
        }, 5000, this)
        console.log('hi!')
    }

    var link = document.querySelector('a');
    link.addEventListener('click', clickNext, true);
})();

