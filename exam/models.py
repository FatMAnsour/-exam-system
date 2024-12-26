from django.db import models
from django.conf import settings
from django.contrib import admin

class Exam (models.Model):
    LEVEL_CHOISE=[
        ("A","Level A"),
        ("B","Level B"),
        ("C","Level C"),
    ]
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=1, choices=LEVEL_CHOISE)

    def __str__(self):
        return self.title

class Question(models.Model):
    ANSWER_CHOISE=[
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
    ]
    exam = models.ForeignKey(Exam , related_name="question", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d  = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOISE)

    def __str__(self):
        return self.title


class Student(models.Model):
    GRADE_CHOISE=[
        ("1","Senior 1"),
        ("2","Senior 2"),
        ("3","Senior 3"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrolling_date = models.DateTimeField(auto_now_add=True)
    grade  = models.CharField(max_length=1, choices=GRADE_CHOISE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}' 

class Answer(models.Model):
    ANSWER_CHOISE=[
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=1, choices= ANSWER_CHOISE)

    def is_correct(self):
       return self.answer  == self.question.correct_answer
    
class Review(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="reviews")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="reviews")
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.exam.title} by {self.user.username}"
   

