function search_teacher(){
    let inputMH = document.getElementById('searchBarMH').value;
    let xMH = document.getElementsByClassName('teacher');
  
    for(i = 0 ; i < xMH.length ; i++){
      if(!xMH[i].innerHTML.includes(inputMH) || inputMH == ''){
        xMH[i].style.display = "none";
      }
      else {
        xMH[i].style.display = "inline-block";
      }
    }
}

const prev = document.getElementById('prev-btn')
const next = document.getElementById('next-btn')
const list = document.getElementById('item-list')
const itemWidth = 290
const padding = 20

prev.addEventListener('click',()=>{
  list.scrollLeft -= (itemWidth + padding)
})
next.addEventListener('click',()=>{
  list.scrollLeft += (itemWidth + padding)
})