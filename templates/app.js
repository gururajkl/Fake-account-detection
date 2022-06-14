const open = document.getElementById('open');
const mc = document.getElementById('model-container');
const close = document.getElementById('close');

open.addEventListener('click', () => {
    mc.classList.add('show');
});

close.addEventListener('click', () => {
    mc.classList.remove('show');
});