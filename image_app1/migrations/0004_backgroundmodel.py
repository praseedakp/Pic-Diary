# Generated by Django 4.2.7 on 2023-12-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app1', '0003_adminimagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='backgroundmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bimage', models.FileField(upload_to='image_app1/static')),
                ('feature', models.CharField(max_length=100)),
            ],
        ),
    ]