document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('header');
    header.addEventListener('click', function() {
        if (header.classList.contains('red')) {
            header.classList.remove('red');
            header.classList.add('green');
        } else {
            header.classList.remove('green');
            header.classList.add('red');
        }
    });
});