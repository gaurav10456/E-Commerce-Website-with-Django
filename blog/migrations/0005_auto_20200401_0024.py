# Generated by Django 3.0.4 on 2020-04-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='head0',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]