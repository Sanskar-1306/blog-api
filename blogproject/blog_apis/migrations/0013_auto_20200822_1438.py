# Generated by Django 3.0.6 on 2020-08-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_apis', '0012_blogmodel_blog_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='blog_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
