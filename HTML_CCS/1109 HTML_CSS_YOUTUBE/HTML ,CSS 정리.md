## ๐HTML ,CSS ์ ๋ฆฌ

> Youtube 'ํ์๊ฐ๋ง์ ๋๋ด๋  HTML/CSS ์๋ฌธ'  ํ๊ธฐ

์ต์ข ํ๋ก์ ํธ ์  ๊น์ง ํ๋ก ํธ ๋ถ๋ถ์์ ์ดํด๋ฅผ ๋ ์๊ธฐ ์ํจ!

***

## Attribute

`Attribute`

- HTML Element์ ์ถ๊ฐ์ ์ธ ์์ฑ์ ๊ด๋ฆฌํ๊ธฐ ์ํ ์์์ด๋ค.

```html
<img style="" width="400px">
<!-- style= , width= ๋ฑ ์ ํตํด ์ถ๊ฐ์ ์ธ ์์ฑ ๊ด๋ฆฌ -->
```

- Attribute๋ HTML Element ๋ง๋ค ์ธ ์ ์๋๊ฒ ๋ค ๋๊ฐ์ง๋ ์๋ค.
  
  - Style ์์ฑ์ด๋ Element ๋์์ธ์ ์ํ

`css๋ฅผ ์ฐ๋ ์ด์ ?`

- ์ ์ฒด ํ์ด์ง Element์ ๋์์ธ์ ํ๋ฒ์ ์ฝ๊ฒ ์ ์ฉํ๊ธฐ ์ํด

- <head> ์ <style> ๋ฅผ ๋ง๋ค์ด ์ค์ 

- class๋ฅผ ์ ์ธํ์ฌ ํ๋ฒ์ ์ ์ฉํ  ์ ์๋ค.

```html
<style>
        .color-primary {          <!-- class ์ ์ธ -->
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

- ๋ํ ์ฌ๋ฌ๊ฐ์ ํด๋์ค๋ฅผ ์ ์ธํ์ฌ ํ๋์ ๋ค ์ ์ธํ  ์ ์๋ค.
  
  - ์ด๋ ํ ๋ฒ์ ์คํ์ผ์ ๋ค ๋ณ๊ฒฝํ  ์ ์์ด ์ ์ฉํ๋ค

- style.css ๋ฅผ ์์ฑํ์ฌ ์ด ๊ณณ ์์ style๊ด๋ฆฌ๋ฅผ ํ  ์ ์๋ค.

```css```
# style.css
.color-primary {
    color:red;
}
.font-50 {
    font-size:50px;
}
```

- <style> ๋ก ์ ์ฉํ ๊ฒ๊ณผ ๊ฐ์ ํจ๊ณผ๋ฅผ ๊ฐ์ง๋ค. ๋ค๋ง

```html
<link rel="stylesheet" href="/ํ์ผ๊ฒฝ๋ก/style.css">
```

์ ๊ฐ์ ๋งํฌ๋ฅผ <head> ์ ์ถ๊ฐํด์ค๋ค.

## Event

- ์นํ์ด์ง ๋ด์์ ํด๋ฆญ,์คํฌ๋กค์ ํ  ๋ ์ด๋ฒคํธ๊ฐ ๋ฐ์

- 
