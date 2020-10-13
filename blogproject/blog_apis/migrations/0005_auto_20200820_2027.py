# Generated by Django 3.0.6 on 2020-08-20 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_apis', '0004_usermodel_following_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='following_data',
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='blogmodel',
            unique_together={('author', 'content')},
        ),
    ]
