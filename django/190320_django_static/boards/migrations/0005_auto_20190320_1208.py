# Generated by Django 2.1.7 on 2019-03-20 12:08

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20190320_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='boards/images'),
        ),
    ]
