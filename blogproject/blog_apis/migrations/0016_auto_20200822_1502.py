# Generated by Django 3.0.6 on 2020-08-22 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_apis', '0015_auto_20200822_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpictures',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog_apis.BlogModel'),
        ),
    ]
