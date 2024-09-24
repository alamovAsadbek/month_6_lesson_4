from django.db import models


class FeedbackModel(models.Model):
    tittle = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()
    status = models.BooleanField(default=False)
    user_firstname = models.CharField(max_length=200)
    user_lastname = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
