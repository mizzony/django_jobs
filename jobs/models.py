from django.db import models
from django import forms

# Create your models here.
#every changes make need to create migrate on terminal
class Job(models.Model):
	COMPANY_CHOICES = [
	    ('Harrots', 'Harrots'),
	    ('Eden', 'Eden'),
	    ('Agen', 'Agen'),
	    ('Adent', 'Adent'),
	 ]

	JOB_TYPE_CHOICES = [
	    ('P', 'Permanent'),
	    ('F', 'Freelance'),
	    ('I', 'Intern'),
	    ('C', 'Contract'),

	]

	CATEGORY_CHOICES = [
	    ('IT', 'Information Technology'),
	    ('HR', 'Human Resource'),
	    ('Mar', 'Marketing'),
	    ('Sale', 'Sales'),
	    ('CS', 'Customer Services'),
	]

	WORK_DAY = [
	    (1, '1 day per week'),
	    (2, '2 day per week'),
	    (3, '3 day per week'),
	    (4, '4 day per week'),
	    (5, '5 day per week'),
	    (6, '6 day per week'),
	    (7, '7 day per week'),
	]

	name       		= models.CharField(max_length=120) #max_length is required
	description 	= models.TextField(blank=False, null=False)
	duty 			= models.TextField(blank=False, null=False, default='')
	email			= models.EmailField(max_length=200, default='') #null = true,default=true
	phone			= models.CharField(max_length=12, default='') #null = true,default=true
	salary			= models.IntegerField(default=0)
	expire_date		= models.DateField()
	active			= models.BooleanField(default=True)
	filled			= models.BooleanField(default=False) #null = true,default=true
	company			= models.CharField(max_length=200, choices=COMPANY_CHOICES, default='Harrots') #null = true,default=true
	job_type		= models.CharField(max_length=1, choices=JOB_TYPE_CHOICES, default='P')
	category		= models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='IT')
	work_day		= models.IntegerField(choices=WORK_DAY, default=5)
	work_time		= models.CharField(max_length=100, default='09:00-17:00')
	benefit 		= models.TextField(blank=True, null=True)
	company_website = models.URLField(max_length=200, default='')
	company_logo	= models.ImageField(upload_to='uploads/company_logo', height_field=None, width_field=None, max_length=200)

class Applicant(models.Model):
	
	EDUCATION_CHOICES = [
	    ('High School', 'High School or Equivalent'),
	    ('Bachelor', 'Bachelor\'s Degree'),
	    ('Master', 'Master\'s Degree'),
	    ('Doctoral', 'Docteral Degrees'),
	]

	name       			= models.CharField(max_length=120, default='')
	education 			= models.TextField(blank=True, null=True)
	email				= models.EmailField(max_length=200, default=None) #null = true,default=true
	phone				= models.CharField(max_length=12, default='') #null = true,default=true
	expected_salary		= models.IntegerField(default=0, blank=True, null=True)
	highest_education	= models.CharField(max_length=200, choices=EDUCATION_CHOICES, default='Bachelor',blank=True, null=True)
	birth_date 			= models.DateField(blank=True, null=True)
	job_id 				= models.ForeignKey('Job', on_delete=models.CASCADE, default=None,blank=True, null=True)
	experience			= models.TextField(blank=True, null=True)
	resume				= models.FileField(upload_to='uploads/resume/', blank=False, null=False)
	transcript			= models.FileField(upload_to='uploads/transcript/', blank=True, null=True)
	image				= models.FileField(upload_to='uploads/image/', blank=True, null=True)


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
        	'name',
        	'email',
        	'phone',
        	'expected_salary',
        	'highest_education',
        	'birth_date',
        	'education',
        	'experience',
        	'resume',
        	'transcript',
        	'image',
        	'job_id',
        ]

        widgets = {
        	'job_id': forms.HiddenInput(),
        	'birth_date': forms.TextInput(
                attrs={'id': 'datepicker'}
            ),
        }









