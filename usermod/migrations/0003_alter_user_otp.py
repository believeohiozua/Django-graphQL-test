# Generated by Django 4.0.3 on 2022-04-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermod', '0002_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(default=2810, max_length=6),
        ),
    ]