const menu = document.querySelector('#menu')
const hamburger = document.querySelector('#hamburger')

hamburger.addEventListener('click',()=>{
    hamburger.querySelector('.b-2').classList.toggle('w-[80%]')
    hamburger.querySelector('.b-2').classList.toggle('relative')
    hamburger.querySelector('.b-2').classList.toggle('-right-3')
    menu.classList.toggle('hidden')
})