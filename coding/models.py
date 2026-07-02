from django.db import models
from django.contrib.auth.models import User


class CodingSubmission(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    language = models.CharField(max_length=30, default="Python")

    question = models.TextField()

    code = models.TextField()

    score = models.IntegerField(default=0)

    execution_time = models.FloatField(default=0)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username