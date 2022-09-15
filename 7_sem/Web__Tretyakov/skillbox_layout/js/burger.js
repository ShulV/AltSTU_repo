let burger = document.querySelector('.header__nav-burger');

burger.addEventListener('click', (e) => {
  document.querySelector('.header__nav-list').classList.toggle('header__nav-list_active');
})
