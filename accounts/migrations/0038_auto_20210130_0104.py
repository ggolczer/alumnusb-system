# Generated by Django 3.0.7 on 2021-01-30 01:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0037_user_information_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile_Picture',
            new_name='ProfilePicture',
        ),
        migrations.RenameModel(
            old_name='User_Achievements',
            new_name='UserAchievements',
        ),
        migrations.RenameModel(
            old_name='User_information',
            new_name='UserInformation',
        ),
        migrations.RenameModel(
            old_name='User_stats',
            new_name='UserStats',
        ),
    ]
