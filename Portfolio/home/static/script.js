const hamburger = document.querySelector('.hamburger');
const hamburger_icon = hamburger.querySelector('span');
const mobile_menu = document.querySelector('.mobile-menu');
const MESSAGEBOX = document.querySelector('.message_text');

hamburger.addEventListener('click', () => {
    hamburger_icon.innerText = hamburger_icon.innerText === 'menu' 
    ? 'close'
    : 'menu';

    console.log('working')

    mobile_menu.classList.toggle('is-open');
})

$('.message_text').hover(function(){
    $('.message_text').animate({
    height: "150px"
  }, {
    duration: 3000,
    specialEasing: {
      width: "linear",
      height: "easeOutBounce"
}});
})