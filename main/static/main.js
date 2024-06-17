navToggler = document.getElementById('nav-toggler');
navLeft = document.getElementById('nav-left');
navLeftOpen = false;
navToggler.addEventListener('click', (e) => {
    console.log('clicked')
    if (navLeftOpen) {
        navToggler.innerHTML = 'Show Menu';
        navLeft.style.display = 'none';
        navLeftOpen = !navLeftOpen
    } else {
        navLeftOpen = !navLeftOpen
        navLeft.style.display = 'block';
        navToggler.innerHTML = 'Collapse Menu';
    }
})
window.addEventListener('resize', (e) => {
    if (window.innerWidth > 576) {
        navLeft.style.display = 'block';
    } else {
        if (navLeftOpen) {
            navLeft.style.display = 'block';
        } else {
            navLeft.style.display = 'none';
        }
        
    }
})