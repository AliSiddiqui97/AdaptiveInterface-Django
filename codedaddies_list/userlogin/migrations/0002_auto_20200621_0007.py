# Generated by Django 2.2.7 on 2020-06-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='country',
            field=models.CharField(default='Pakistan', max_length=100, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='userlogin',
            name='dob',
            field=models.CharField(default='20-APR-1997', max_length=100, verbose_name='DOB'),
        ),
    ]
