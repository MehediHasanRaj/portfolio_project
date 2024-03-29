# Generated by Django 5.0.1 on 2024-02-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='role',
            field=models.CharField(default='Software Engineer', max_length=20),
        ),
        migrations.AlterField(
            model_name='profil',
            name='images',
            field=models.ImageField(upload_to='portfolio/static/profile/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/static/project/'),
        ),
    ]
