from django.shortcuts import render,get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects.all()
    return render(request,'home.html',{'jobs':jobs})

def details(request, id):
    job_detail = get_object_or_404(Job,pk = id)
    return render(request,'details.html',{'job':job_detail})

