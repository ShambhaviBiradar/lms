# Generated by Django 2.1.3 on 2018-11-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
