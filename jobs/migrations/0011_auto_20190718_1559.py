# Generated by Django 2.2.3 on 2019-07-18 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20190718_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='job_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='highest_education',
            field=models.CharField(choices=[('High School', 'High School or Equivalent'), ('Bachelor', "Bachelor's Degree"), ('Master', "Master's Degree"), ('Doctoral', 'Docteral Degrees')], default='Bachelor', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='image',
            field=models.FileField(upload_to='uploads/image/'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(upload_to='uploads/resume/'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='transcript',
            field=models.FileField(upload_to='uploads/transcript/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_logo',
            field=models.FileField(upload_to='uploads/company_logo'),
        ),
    ]
