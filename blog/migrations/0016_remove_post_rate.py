# Generated by Django 3.0 on 2021-03-02 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210301_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rate',
        ),
    ]