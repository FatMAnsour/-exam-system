# Generated by Django 5.1.4 on 2024-12-21 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='descroption',
            new_name='description',
        ),
    ]
