# Generated by Django 4.1.2 on 2022-10-18 04:35

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('title', 'author__user__username'), unique=True, verbose_name='slug'),
        ),
    ]
