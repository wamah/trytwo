# Generated by Django 2.2.1 on 2021-02-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='prof',
            name='location',
            field=models.CharField(default='location default', max_length=120),
        ),
    ]
