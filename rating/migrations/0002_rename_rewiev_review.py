# Generated by Django 3.2 on 2022-08-19 12:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rewiev',
            new_name='Review',
        ),
    ]