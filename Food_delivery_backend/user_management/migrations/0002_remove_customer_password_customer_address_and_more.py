# Generated by Django 5.0.3 on 2024-06-02 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
    ]