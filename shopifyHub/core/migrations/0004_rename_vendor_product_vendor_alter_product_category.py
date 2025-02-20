# Generated by Django 5.0.2 on 2024-04-21 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='vendor',
            new_name='Vendor',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category'),
        ),
    ]
