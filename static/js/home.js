let imgIndex = 0;

function autoSlide(){
  let x = document.getElementsByClassName('mySlides');
  for(var i=0;i<x.length;i++ ){
    x[i].style.display = 'none';
  }
  if(imgIndex == x.length-1){
    imgIndex = 0;
  }
  x[imgIndex].style.display = 'block';
  imgIndex++;
  setTimeout(autoSlide,3000);
}

autoSlide();
