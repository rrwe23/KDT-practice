## 📗HTML ,CSS 정리

> Youtube '한시간만에 끝내는  HTML/CSS 입문'  필기

최종 프로젝트 전 까지 프론트 부분에서 이해를 더 쌓기 위함!

***

## Attribute

`Attribute`

- HTML Element의 추가적인 속성을 관리하기 위한 요소이다.

```html
<img style="" width="400px">
<!-- style= , width= 등 을 통해 추가적인 속성 관리 -->
```

- Attribute는 HTML Element 마다 쓸 수 있는게 다 똑같지는 않다.
  
  - Style 속성이란 Element 디자인을 입힘

`css를 쓰는 이유?`

- 전체 페이지 Element에 디자인을 한번에 쉽게 적용하기 위해

- <head> 속 <style> 를 만들어 설정

- class를 선언하여 한번에 적용할 수 있다.

```html
<style>
        .color-primary {          <!-- class 선언 -->
            color:red;
        }
    </style>
</head>
<body>
    <h1>My First Heading</h1>
    <p class="color-primary" >My First Paragraph</p> 
    <p style="color:blue;">My First Paragraph</p> 
    <p style="font-size:30px;">My First Paragraph</p> 
```

- 또한 여러개의 클래스를 선언하여 하나에 다 선언할 수 있다.
  
  - 이는 한 번에 스타일을 다 변경할 수 있어 유용하다

- style.css 를 생성하여 이 곳 에서 style관리를 할 수 있다.

```css```
# style.css
.color-primary {
    color:red;
}
.font-50 {
    font-size:50px;
}
```

- <style> 로 적용한 것과 같은 효과를 가진다. 다만

```html
<link rel="stylesheet" href="/파일경로/style.css">
```

와 같은 링크를 <head> 에 추가해준다.

## Event

- 웹페이지 내에서 클릭,스크롤을 할 때 이벤트가 발생

- 
