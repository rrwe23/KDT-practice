# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

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

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where age < 10;
```

```

```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where gender = 1;
```

```

```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where (smoking=3 AND is_drinking=1);
```

```

```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where (va_left >= 2.0 AND va_right >= 2.0);
```

```

```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
select sido from healthcare;
```

```

```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 85이상이면서 몸무게가 80이하인 사람

```python
select count(*) from healthcare where (waist >= 85 and weight >= 80);
```

> 키가 185 이상 또는 몸무게가 85 이상이면서 왼쪽 눈 시력이 1.0 이상인 사람

```python
select count(*) from healthcare where(height >= 185 OR weight >= 85)AND va_left >= 1.0;
```