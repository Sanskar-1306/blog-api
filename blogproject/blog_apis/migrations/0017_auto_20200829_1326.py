# Generated by Django 3.0.6 on 2020-08-29 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_apis', '0016_auto_20200822_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_apis.BlogModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersaved', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-saved'],
                'unique_together': {('blog', 'user')},
            },
        ),
        migrations.DeleteModel(
            name='BlogPictures',
        ),
    ]
