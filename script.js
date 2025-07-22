document.getElementById('show-signup').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelectorAll('.form-box').forEach(box => {
        box.classList.toggle('hidden');
    });
});

document.getElementById('show-login').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelectorAll('.form-box').forEach(box => {
        box.classList.toggle('hidden');
    });
});