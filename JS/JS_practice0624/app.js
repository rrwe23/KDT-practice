// const hellos = document.getElementsByClassName("h1");
// console.log(hellos)

// const h2 = document.getElementsByClassName("h2")
// console.log(h2)

// const h3 = document.getElementById("H3")
// console.log(h3)

// querySelector = Element를 CSS방식으로 검색가능

// const title = document.querySelector(".hello h1");
//  // 여러개가 존재해도 하나만 가져옴


// console.log(title)

// const title2 = document.querySelectorAll(".hello h1");
// // 여러개 다 가져옴
// console.log(title2)

const title = document.querySelector("div.hello:first-child h1");
// console.log(title)
// title.innerText = "Hello";

console.dir(title);
title.style.color="blue";
function handleTitleClick() {
    // console.log("title was clicked!");
    title.style.color = "red"
}

function handleMouseEnter() {
    title.innerText = "Mouse is here"
}

function handleMouseLeave() {
    title.innerText = "Mouse is gone"
}
function handleWindowResize() {
    document.body.style.backgroundColor = "blue";
}

function handleWindowCopy() {
    alert("훔쳐가지마!")
}

function noWifi() {
    alert("인터넷 안됨 ㅜㅜ")
}
function haveWifi() {
    alert("이제 됨 ㅎㅎ")
}
title.addEventListener("click",handleTitleClick);
title.addEventListener("mouseenter",handleMouseEnter);
title.addEventListener("mouseleave",handleMouseLeave);

window.addEventListener("resize",handleWindowResize);
window.addEventListener("copy",handleWindowCopy);
window.addEventListener("offline",noWifi);
window.addEventListener("online",haveWifi);