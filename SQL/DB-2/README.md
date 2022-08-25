# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare
sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,
    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
select count(*) from healthcare
```

```

```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오.

```sql
select max(age) from healthcare
```

```
select min(age) from healthcare
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
select max(height),max(weight) from healthcare
```

```
select min(height),min(weight) from healthcare
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
select count(*) from healthcare where height >= 160 and height >= 170;
```

```

```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오.

```sql
SELECT id ,waist from healthcare WHERE is_drinking = 1 AND waist !='' ORDER BY waist DESC LIMIT 5;
```

```
.header on / .mode column
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where va_left >= 1.5 and va_right >=1.5 and is_drinking =1;
```

```

```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where blood_pressure < 120;
```

```

```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
select avg(waist) from healthcare where blood_pressure >= 140;
```

```

```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
select avg(height),avg(weight) from healthcare where gender = 1;
```

```

```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
select id,height,weight from healthcare where max(height);
```

```

```

### 11. BMI가 30이상인 사람의 수를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
select count(*) from healthcare where (weight/((height * height)*0.0001)) >= 30;
```

```
(weight/((height * height)*0.0001) AS BMI 로 사용가능
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
select id,weight/((height * height)*0.0001) AS BMIfrom healthcare where smoking = 3 order by BMI DESC LIMIT 5; 
```

```

```

### 13. (자유) 술을 마시면서 흡연 지수 1이상인 사람의 수

```sql
SELECT count(*) FROM healthcare WHERE is_drinking = 1 AND smoking >= 1;
```

```
count(*)
--------
584685
```

### 14. (자유) 양쪽 시력 모두 1.0 미만인 사람의 수

```sql
SELECT COUNT(*) FROM healthcare WHERE (va_left < 1.0 AND va_right < 1.0);
```

```
COUNT(*)
--------
432797
```

### 15.(자유) 키가 180 이상 200 이하이면서 몸무게가 80 kg 이상인 사람의 수

```sql
SELECT COUNT(*) FROM healthcare WHERE (height  BETWEEN 180 AND 200) AND (weight >= 80);
```

```
COUNT(*)
--------
18786
```
