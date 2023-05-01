# Generated by Django 4.2 on 2023-04-29 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=32, unique=True)),
                ('gender', models.CharField(choices=[('H', 'Homme'), ('F', 'Female')], max_length=1)),
                ('date_arrivee', models.DateField(null=True)),
                ('date_depart', models.DateField(null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='role.role')),
            ],
        ),
        migrations.CreateModel(
            name='TaskByPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
                ('task', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbrheures', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='person.taskbyperson')),
            ],
        ),
    ]
