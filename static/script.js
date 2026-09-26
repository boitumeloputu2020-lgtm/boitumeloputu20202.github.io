const menu = document.querySelector('.menu');
const nav = document.querySelector('.header nav');
menu?.addEventListener('click', () => nav.classList.toggle('open'));
document.querySelectorAll('nav a').forEach((link) => link.addEventListener('click', () => nav.classList.remove('open')));
