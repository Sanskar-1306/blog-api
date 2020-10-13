# Generated by Django 3.0.6 on 2020-08-20 09:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_apis', '0003_followersandfollowing'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='following_data',
            field=models.ManyToManyField(blank=True, related_name='_usermodel_following_data_+', to=settings.AUTH_USER_MODEL),
        ),
    ]