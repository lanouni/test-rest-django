# Generated by Django 4.2 on 2023-05-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
