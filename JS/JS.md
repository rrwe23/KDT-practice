## 

## HTML에서 출력

```html
<script type = "text/javascript">
    document.write('Coding everybody <br/>');
</script>  
# 스크립트를 통해  HTML에 표기
```

```html
<script type = "text/javascript">
    while(true){  # while 의 조건 동안 아래의 문장을 계속 출력
    document.write("Coding everybody <br />");
}
</script>  
# while 문을 정지않고 반복시키면 무한 루프에 빠진다.
```

```html
<script type = "text/javascript">
    while(i < 10){  # 조건을 넣어 무한반복을 피한다.)
    document.write("Coding everybody <br />");
    i = i + 1
}
</script> 
```
