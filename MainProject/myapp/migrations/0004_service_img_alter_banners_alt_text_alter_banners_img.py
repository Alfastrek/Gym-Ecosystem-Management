# Generated by Django 5.0.2 on 2024-03-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_banners_alt_text_alter_service_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(null=True, upload_to='services/'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='alt_text',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='banners',
            name='img',
            field=models.ImageField(upload_to='D:\\gympro\\myprojectenv\\GYMAG\\media\x08anners/'),
        ),
    ]