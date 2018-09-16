let ham = document.querySelector('.ham');
ham.textContent = '\u2630';
//&#8801
let dropdown = document.querySelector('.nav-dropdown');

ham.addEventListener('click',() =>{

  if(dropdown.style.display == 'none'){
    dropdown.style.display = 'block';
    ham.innerHTML = '&times;';
  }else{
    dropdown.style.display = 'none';
    ham.textContent = '\u2630';
  }
});
