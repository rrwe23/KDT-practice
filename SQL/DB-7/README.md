# 데이터베이스 07 - ORM

💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()
class Genre(models.Model):
    title = models.TextField()
```

```
### 2. 모델을 마이그레이트(migrate) 하세요.
```

# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.

```bash
python manage.py makemigrations
```

### 3. Queryset 메소드 `create` 를 활용해서 `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name            | debut      | country |
| --------------- | ---------- | ------- |
| 봉준호             | 1993-01-01 | KOR     |
| 김한민             | 1999-01-01 | KOR     |
| 최동훈             | 2004-01-01 | KOR     |
| 이정재             | 2022-01-01 | KOR     |
| 이경규             | 1992-01-01 | KOR     |
| 한재림             | 2005-01-01 | KOR     |
| Joseph Kosinski | 1999-01-01 | KOR     |
| 김철수             | 2022-01-01 | KOR     |

```python
director = Director()

In [2]: director.name = '봉준호'

In [3]: director.debut = '1993-01-01'

In [4]: director.country = 'KOR'

In [5]: director.save()


Director.objects.create(name='김한민',debut='1999-01-01',country = 'KOR')
Director.objects.create(name='최동훈',debut='2004-01-01',country = 'KOR')
Director.objects.create(name='이정재',debut='2022-01-01',country = 'KOR')
Director.objects.create(name='이경규',debut='1992-01-01',country = 'KOR')
Director.objects.create(name='Joseph Kosinski',debut='1999-01-01',country = 'KOR')'
Director.objects.create(name='김철수',debut='2022-01-01',country = 'KOR')
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| ----- |
| 액션    |
| 드라마   |
| 사극    |
| 범죄    |
| 스릴러   |
| SF    |
| 무협    |
| 첩보    |
| 재난    |

> genre = Genre()
> 
> enre.title = '액션'
> 
> Genre.objects.create(title='드라마')
> 
> Genre.objects.create(title='사극')
> 
> Genre.objects.create(title='범죄')
> 
> Genre.objects.create(title='스릴러')
> 
> Genre.objects.create(title='SF')
> 
> Genre.objects.create(title='무협')
> 
> Genre.objects.create(title='첩보')
> 
> Genre.objects.create(title='재난')

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성

```pythonag-0-1gb6mdehuag-1-1gb6mdehu
ag-0-1gb6mdehuag-0-1gb6mdehuDirectors = Director.objects.all()

for Director in Directors:
    print(Director.name,Director.debut,Director.country)ag-1-1gb6mdehuag-1-1gb6mdehu
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성

```python
target = Director.objects.get(id=1)
print(target.name,target.debut,target.country)
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> Director.objects.all().get(country="USA")

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> DoesNotExist: Director matching query does not exist.

> country 가 'USA' 인 쿼리가 존재하지 않기 때문

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서 `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성

```python
target = Director.objects.get(name = 'Joseph Kosinski')
target.country = 'USA'
target.save()
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성

```python
target = Director.objects.get(country = 'KOR')
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지

```python
MultipleObjectsReturned: get() returned more than one Director -- 
it returned 7!
```

> 이유 작성

```python
get()으로 인한 리턴값은 1을 넘으면 안되는데 리턴값이 7이기 때문이다.
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성

```python
target = Director.objects.filter(country = 'KOR')
for i in target:
    print(i.name,i.debut,i.country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

> get은 단일 객체를 특정할 때 사용
> 
> filter 는 목록값을 리스트로 가져오면서 1개 이상의 값을 특정할 때 유용

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서 `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> director = Director.objects.get(name='김철수')
> 
> director.delete()
