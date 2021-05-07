from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=150)
    roll_no = models.IntegerField(unique=True)
    subject_1 = models.CharField(max_length=16, choices=[["English","English"]])
    subject_2 = models.CharField(max_length=16, choices=[["Maths","Maths"]])
    subject_3 = models.CharField(max_length=16, choices=[["Science","Science"]])
    subject_4 = models.CharField(max_length=12, choices= [["Tamil", "Tamil"],["French", "French"],["Hindi", "Hindi"]])

    def __str__(self):
        return self.name

class Add_Mark(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="add",unique=True)
    english = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    maths = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    science = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    elective = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return str(self.name)