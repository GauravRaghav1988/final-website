# Generated by Django 4.2.7 on 2023-11-27 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='name',
            new_name='heading',
        ),
    ]
