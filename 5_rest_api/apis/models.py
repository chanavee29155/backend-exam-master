from django.db import models

from apis.choices import Gender


class School(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    grade_level = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    class Meta:
        unique_together = ('school', 'grade_level', 'section')

    def __str__(self):
        return f"{self.school.name} - {self.grade_level}/{self.section}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
