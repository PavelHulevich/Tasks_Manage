# Generated by Django 3.2.22 on 2024-03-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userstasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_of_create',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='deadline',
            field=models.CharField(max_length=25),
        ),
    ]
