# Generated by Django 4.2.11 on 2024-05-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=123)),
                ('phone_number', models.CharField(max_length=13)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'courses',
                'verbose_name_plural': 'coursess',
            },
        ),
    ]
