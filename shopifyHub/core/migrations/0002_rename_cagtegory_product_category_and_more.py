# Generated by Django 5.0.2 on 2024-04-20 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cagtegory',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]
