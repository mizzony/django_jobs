# Generated by Django 2.2.3 on 2019-07-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20190717_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Adent', 'Adent')], default='Junior', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Adent', 'Adent')], default='Freshman', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Adent', 'Adent')], default='Sophomore', max_length=200),
        ),
    ]
