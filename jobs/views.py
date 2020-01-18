from django.shortcuts import render
from django.http import HttpResponse
from .models import Job, Applicant, ApplicantForm

# Create your views here.
#handle your variable pages

def home_view(request, *args, **kwargs):
	return render(request, 'home.html') #string of html code

def company_view(request, *args, **kwargs):
	job_type = request.GET.get('job_type')
	jobs = Job.objects.filter(job_type=job_type)

	return render(request, 'company.html', {
		'jobs': jobs
	})

def job_detail_view(request, id):
	job = Job.objects.get(pk=id)
	print(job)

	return render(request, job.job_type == 'P' and 'job_detail_permanent.html' or 'job_detail_freelance.html', {
		'job': job
	})

def apply_form(request, id):
	form = ApplicantForm(request.POST or None, request.FILES or None, initial={'job_id': Job.objects.get(pk=id)})
	print(request.POST)
	print(request.FILES)
	print(form.is_valid())
	print(form.errors)
	if form.is_valid():
		form.save()

	return render(request, 'apply_form.html', {'form': form})