## 📗M : N

***

`만약 병원 예약 시스템 구축을 위한 DB 모델링을 진행한다면?`

- 진료과목? , 의사정보, 환자 정보, 예약시간.

`RDB`

- 1:1
  
  - 한 테이블의 레코드 1개가 다른 테이블의 레코드 단 한개와 관련

- N:1
  
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우

- M:N
  
  - 양쪽 모두에서 N:1 관계를 가짐
  
  - 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련

`N:1의 한계`

> 한 명의 의사에게 여러 환자가 예약할 수 있다고 설정

```python
# hospitals/ models.py
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctor models.ForeignKey(doctor, on_delete=models.CASCADE)
    name = models.TextField()


    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

이후 Migration 진행

```python
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py shell_plus
```

`but, 동시 예약이 힘들다`

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성

- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

```python
# hospitals/ models.py
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor models.ForeignKey(doctor, on_delete=models.CASCADE)
    patient = models.Foreignkey(Patient, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환'
```

`migrations 이후`

```python
# 의사와 환자 생성 후 예약 만들기
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')


Reservation.create(doctor=doctor1, patient=patient1)
```

` 이후 예약 정보를 조회`

```python
doctor1.reservation_set.all() # 의사, 예약 정보 찾기
patient1.reservation_set.all() # 환자, 예약 정보 찾기
```

### Django manyToManyField

환자 모델에 작성

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor):
    name = models.TextField()

    def__str__(self):
        return f'{self.pk}번 환자

# make migrations
```

- 이후 생성된 중개 테이블을 확인한다.

![](C:\Users\이주현\AppData\Roaming\marktext\images\2022-10-24-15-06-42-image.png)



- 의사 1명과 환자 2명 생성

```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

N:1 모델은 한계가 있다...

`ManyToManyField`

```python
p1.doctors.all() # 환자 1이 만난 의사들
p1.reservation_set.all() #
```

```python
path
```

get vs filter

get : 한개 있으면 그 객체를 줌

근데 없으면 오류, 많아도 오류

즉, 하나의 객체를 확인할 때 사용

가지고 오더라고 그 객체

filter : 쿼리셋이다. 무조건 0개든 많이 있든
