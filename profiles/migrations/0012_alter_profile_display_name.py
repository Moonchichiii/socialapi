# Generated by Django 5.0.4 on 2024-05-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_profile_options_profile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]