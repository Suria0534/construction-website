from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Project, About, ContactMessage
from django.db.models import Q
from .models import Project

# Home page showing all projects
def home(request):
    projects = Project.objects.all()
    completed_projects_count = Project.objects.filter(is_completed=True).count()
    return render(request, 'main/home.html', {
        'projects': projects,
        'completed_projects_count': completed_projects_count,
    })

# Project detail page
def project_detail(request, pk):
    # 'pk' parameter ta ekhane thakte hobe, karon URL theke 'pk' pathano hocche
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})


# All project list
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})

# ✅ Search view fixed
def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        query = query.strip()
        results = Project.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'main/search_results.html', {'results': results, 'query': query})

# About page
def about(request):
    about_content = About.objects.first()
    return render(request, 'main/about.html', {'about': about_content})

# Contact page with form submission
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(name=name, email=email, message=message)
        return render(request, 'main/contact.html', {'success': True})
    return render(request, 'main/contact.html')

# User registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after successful registration
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

# User login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

# User logout
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

# Dashboard - requires login
@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

# Privacy policy
def privacy_policy(request):
    return render(request, 'main/privacy.html')
