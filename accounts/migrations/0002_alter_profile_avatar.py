# Generated by Django 4.1.2 on 2022-10-18 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', upload_to='avatars/'),
        ),
    ]
