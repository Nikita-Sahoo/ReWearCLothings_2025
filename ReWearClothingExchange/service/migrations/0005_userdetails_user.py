# Generated by Django 4.1 on 2025-07-12 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_item_condition_item_size_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(to='service.login', on_delete=models.CASCADE, default=1),
            preserve_default=False,
        ),
    ]
