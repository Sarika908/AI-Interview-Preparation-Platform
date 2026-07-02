from django.db import models


class Question(models.Model):
    CATEGORY_CHOICES = [
        ("Python", "Python"),
        ("Django", "Django"),
        ("SQL", "SQL"),
        ("AWS", "AWS"),
        ("AI", "AI"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    question = models.TextField()

    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question