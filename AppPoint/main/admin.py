from django.contrib import admin
from .models import Tasks, UserTaskSubmission

admin.site.register(Tasks)
admin.site.register(UserTaskSubmission)