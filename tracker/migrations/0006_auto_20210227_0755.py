# Generated by Django 3.1.7 on 2021-02-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20210227_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='risk',
            field=models.CharField(choices=[('-', '-'), ('OK', 'OK')], max_length=100, null=True),
        ),
    ]
