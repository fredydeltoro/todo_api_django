# Generated by Django 4.2.6 on 2023-10-23 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_todolist_created_todolist_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='modified',
            new_name='updated_at',
        ),
    ]