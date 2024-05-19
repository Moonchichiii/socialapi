# Generated by Django 5.0.4 on 2024-05-17 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
        ('profiles', '0015_remove_profile_followers'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='follower',
            name='follower',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='profiles.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follower',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='profiles.profile'),
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user',
        ),
    ]
