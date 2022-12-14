## πM : N

***

`λ§μ½ λ³μ μμ½ μμ€ν κ΅¬μΆμ μν DB λͺ¨λΈλ§μ μ§ννλ€λ©΄?`

- μ§λ£κ³Όλͺ©? , μμ¬μ λ³΄, νμ μ λ³΄, μμ½μκ°.

`RDB`

- 1:1
  
  - ν νμ΄λΈμ λ μ½λ 1κ°κ° λ€λ₯Έ νμ΄λΈμ λ μ½λ λ¨ νκ°μ κ΄λ ¨

- N:1
  
  - ν νμ΄λΈμ 0κ° μ΄μμ λ μ½λκ° λ€λ₯Έ νμ΄λΈμ λ μ½λ ν κ°μ κ΄λ ¨λ κ²½μ°

- M:N
  
  - μμͺ½ λͺ¨λμμ N:1 κ΄κ³λ₯Ό κ°μ§
  
  - 0κ° μ΄μμ λ μ½λκ° λ€λ₯Έ νμ΄λΈμ 0κ° μ΄μμ λ μ½λμ κ΄λ ¨

`N:1μ νκ³`

> ν λͺμ μμ¬μκ² μ¬λ¬ νμκ° μμ½ν  μ μλ€κ³  μ€μ 

```python
# hospitals/ models.py
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}λ² μμ¬ {self.name}'

class Patient(models.Model):
    doctor models.ForeignKey(doctor, on_delete=models.CASCADE)
    name = models.TextField()


    def __str__(self):
        return f'{self.pk}λ² νμ {self.name}'
```

μ΄ν Migration μ§ν

```python
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py shell_plus
```

`but, λμ μμ½μ΄ νλ€λ€`

- νμ λͺ¨λΈμ μΈλ ν€λ₯Ό μ­μ νκ³  λ³λμ μμ½ λͺ¨λΈμ μλ‘ μμ±

- μμ½ λͺ¨λΈμ μμ¬μ νμμ κ°κ° N:1 κ΄κ³λ₯Ό κ°μ§

```python
# hospitals/ models.py
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}λ² νμ {self.name}'

class Reservation(models.Model):
    doctor models.ForeignKey(doctor, on_delete=models.CASCADE)
    patient = models.Foreignkey(Patient, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.doctor_id}λ² μμ¬μ {self.patient_id}λ² ν'
```

`migrations μ΄ν`

```python
# μμ¬μ νμ μμ± ν μμ½ λ§λ€κΈ°
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')


Reservation.create(doctor=doctor1, patient=patient1)
```

` μ΄ν μμ½ μ λ³΄λ₯Ό μ‘°ν`

```python
doctor1.reservation_set.all() # μμ¬, μμ½ μ λ³΄ μ°ΎκΈ°
patient1.reservation_set.all() # νμ, μμ½ μ λ³΄ μ°ΎκΈ°
```

### Django manyToManyField

νμ λͺ¨λΈμ μμ±

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor):
    name = models.TextField()

    def__str__(self):
        return f'{self.pk}λ² νμ

# make migrations
```

- μ΄ν μμ±λ μ€κ° νμ΄λΈμ νμΈνλ€.

![](C:\Users\μ΄μ£Όν\AppData\Roaming\marktext\images\2022-10-24-15-06-42-image.png)



- μμ¬ 1λͺκ³Ό νμ 2λͺ μμ±

```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

N:1 λͺ¨λΈμ νκ³κ° μλ€...

`ManyToManyField`

```python
p1.doctors.all() # νμ 1μ΄ λ§λ μμ¬λ€
p1.reservation_set.all() #
```

```python
path
```

get vs filter

get : νκ° μμΌλ©΄ κ·Έ κ°μ²΄λ₯Ό μ€

κ·Όλ° μμΌλ©΄ μ€λ₯, λ§μλ μ€λ₯

μ¦, νλμ κ°μ²΄λ₯Ό νμΈν  λ μ¬μ©

κ°μ§κ³  μ€λλΌκ³  κ·Έ κ°μ²΄

filter : μΏΌλ¦¬μμ΄λ€. λ¬΄μ‘°κ±΄ 0κ°λ  λ§μ΄ μλ 
