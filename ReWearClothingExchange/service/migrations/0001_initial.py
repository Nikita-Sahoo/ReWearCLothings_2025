# Generated by Django 4.1 on 2025-07-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('c_password', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
