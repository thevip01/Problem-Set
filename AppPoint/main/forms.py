from django import forms
from .models import Tasks, UserTaskSubmission

# Form to create a task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['app_name', 'link', 'category', 'sub_category', 'points']
        widgets = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'class': 'form-control'}),
            'points': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Form to handle task submission
class TaskSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserTaskSubmission
        fields = ['screenshot']
        widgets = {
            'screenshot': forms.FileInput(attrs={'class': 'form-control'}),
        }
