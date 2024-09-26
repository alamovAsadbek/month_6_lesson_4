from django.db import models


class FeedbackModel(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()
    status = models.BooleanField(default=False)
    user_firstname = models.CharField(max_length=200)
    user_lastname = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedbacks"
        verbose_name = "Feedback"

    def __str__(self):
        return self.title
