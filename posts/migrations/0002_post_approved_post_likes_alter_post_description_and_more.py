# Generated by Django 5.0.4 on 2024-05-13 20:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='ingredients',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='recipe',
            field=models.TextField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
