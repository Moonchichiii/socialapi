# Generated by Django 5.0.4 on 2024-05-17 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0002_alter_follower_unique_together_follower_follower_and_more'),
        ('profiles', '0015_remove_profile_followers'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('profile', 'follower')},
        ),
    ]