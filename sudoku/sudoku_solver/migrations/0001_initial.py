# Generated by Django 3.0.1 on 2020-01-09 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('task_selected', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('task_outcome', models.CharField(max_length=20)),
            ],
        ),
    ]
