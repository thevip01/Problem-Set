from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Entertainment', 'Entertainment'),
    ('Education', 'Education'),
    ('Lifestyle', 'Lifestyle'),
    ('Social Media', 'Social Media'),
]

SUBCATEGORY_CHOICES = [
    ('Games', 'Games'),
    ('Videos', 'Videos'),
    ('News', 'News'),
    ('Chat', 'Chat'),
    ('Learning', 'Learning'),
    ('Health', 'Health'),
]

class Tasks(models.Model):
    app_name = models.CharField(max_length=255)
    link = models.URLField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=100, choices=SUBCATEGORY_CHOICES)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_name

class UserTaskSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='submissions')
    screenshot = models.ImageField(upload_to='screenshots/')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.app.app_name}"
