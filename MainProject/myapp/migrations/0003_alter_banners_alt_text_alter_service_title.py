# Generated by Django 5.0.2 on 2024-03-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_banners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners',
            name='alt_text',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
