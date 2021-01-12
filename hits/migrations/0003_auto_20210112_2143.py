# Generated by Django 3.1.5 on 2021-01-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hits', '0002_hitman_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hitman',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='hitman',
            name='last_name',
        ),
        migrations.AddField(
            model_name='hitman',
            name='name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]