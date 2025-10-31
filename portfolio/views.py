
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact

def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'featured_projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('portfolio:contact')
    
    return render(request, 'portfolio/contact.html')