# Generated by Django 2.1.7 on 2019-03-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
