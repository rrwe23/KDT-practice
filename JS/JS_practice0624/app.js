// const hellos = document.getElementsByClassName("h1");
// console.log(hellos)

// const h2 = document.getElementsByClassName("h2")
// console.log(h2)

// const h3 = document.getElementById("H3")
// console.log(h3)

// querySelector = Element를 CSS방식으로 검색가능

const title = document.querySelector(".hello h1");
 // 여러개가 존재해도 하나만 가져옴


console.log(title)

const title2 = document.querySelectorAll(".hello h1");
// 여러개 다 가져옴
console.log(title2)