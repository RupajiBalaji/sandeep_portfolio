from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import FileResponse
from django.conf import settings
import os
from .models import Skill, Project, Experience, Education, Certification, ContactMessage
from .forms import ContactForm


def download_resume(request):
    """Download resume file"""
    # Try to find resume file (check for both .txt and .pdf)
    resume_txt_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'portfolio', 'files', 'resume.txt')
    resume_pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'portfolio', 'files', 'resume.pdf')
    
    # Check if PDF exists first
    if os.path.exists(resume_pdf_path):
        return FileResponse(
            open(resume_pdf_path, 'rb'),
            as_attachment=True,
            filename='Shalem_Sandeep_Resume.pdf'
        )
    # Fall back to text file
    elif os.path.exists(resume_txt_path):
        return FileResponse(
            open(resume_txt_path, 'rb'),
            as_attachment=True,
            filename='Shalem_Sandeep_Resume.txt'
        )
    else:
        # If no resume file, return error message
        from django.http import HttpResponse
        response = HttpResponse(
            "Resume file not available. Please check back soon!",
            content_type='text/plain',
            status=404
        )
        return response


def home(request):
    """Home page view"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    experiences = Experience.objects.all()[:3]
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'portfolio/home.html', context)


def portfolio(request):
    """Portfolio page with all projects"""
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/portfolio.html', context)


def about(request):
    """About page"""
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'experiences': experiences,
        'education': education,
        'certifications': certifications,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)


def project_detail(request, pk):
    """Project detail page"""
    project = Project.objects.get(pk=pk)
    other_projects = Project.objects.exclude(pk=pk)[:3]
    
    context = {
        'project': project,
        'other_projects': other_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)


def contact(request):
    """Contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': ContactForm(),
                'success': True,
            }
            return render(request, 'portfolio/contact.html', context)
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'portfolio/contact.html', context)
