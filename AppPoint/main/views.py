from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Tasks, UserTaskSubmission
from .forms import TaskForm, TaskSubmissionForm

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    
    tasks = Tasks.objects.all()    
    return render(request, 'admin_dashboard.html', {'tasks': tasks})

@login_required
def user_dashboard(request):
    tasks = Tasks.objects.prefetch_related('submissions').filter(
        submissions__completed=False
    ).distinct()
    return render(request, 'user_dashboard.html', {'tasks': tasks})

@login_required
def submit_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TaskSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.app = task
            submission.completed = True
            submission.save()
            messages.success(request, 'Task submitted successfully!')
            return redirect('user_dashboard')
    else:
        form = TaskSubmissionForm()
    
    return render(request, 'submit_task.html', {'form': form, 'task': task})

def admin_dashboard(request):
    tasks = Tasks.objects.all()
    return render(request, 'admin_dashboard.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('admin_dashboard')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def view_submissions(request):
    submissions = UserTaskSubmission.objects.all()
    return render(request, 'view_submissions.html', {'submissions': submissions})

def user_dashboard(request):
    tasks = Tasks.objects.all()
    return render(request, 'user_dashboard.html', {'tasks': tasks})

def view_points(request):
    user_points = UserTaskSubmission.objects.filter(user=request.user, completed=True).all()
    total_points = sum(submission.app.points for submission in user_points)

    return render(request, 'points.html', {'points': user_points, 'total_points': total_points})

def completed_tasks(request):
    completed_tasks = UserTaskSubmission.objects.filter(user=request.user, completed=True)
    return render(request, 'completed_tasks.html', {'tasks': completed_tasks})

def logout_view(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_dashboard")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")