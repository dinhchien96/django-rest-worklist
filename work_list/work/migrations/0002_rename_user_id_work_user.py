# Generated by Django 4.0.7 on 2022-10-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='user_id',
            new_name='user',
        ),
    ]