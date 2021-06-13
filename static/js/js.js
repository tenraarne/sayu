const navSlide = () => {
    const menu = document.querySelector('.menu');
    const mobile_navbar_div = document.querySelector('.mobile_navbar_div');
    const mobile_navbar  = document.querySelector('.mobile_navbar');
    menu.addEventListener('click',()=>{
       mobile_navbar_div.classList.toggle('mobile_navbar_active');
       mobile_navbar.classList.toggle('mobile_navbar_items_active');
    });
}
function displaySize(){
    var res = window.innerWidth + "x" + window.innerHeight;
    document.getElementById("result").innerHTML = res;

}


displaySize();
navSlide();