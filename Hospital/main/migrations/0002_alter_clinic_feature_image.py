# Generated by Django 4.1.7 on 2023-02-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='feature_image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
