from django.db import models
from django.contrib.auth.models import User


class InterviewSession(models.Model):
    CATEGORY_CHOICES = [
        ("Python", "Python"),
        ("Django", "Django"),
        ("SQL", "SQL"),
        ("AWS", "AWS"),
        ("HR", "HR"),
        ("AI", "AI/ML"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    question = models.TextField()
    answer = models.TextField()
    feedback = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category}"