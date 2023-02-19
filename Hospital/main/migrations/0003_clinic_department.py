# Generated by Django 4.1.7 on 2023-02-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_clinic_feature_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='department',
            field=models.CharField(choices=[('HEART_CENTER', 'Heart Center'), ('NEUROSCIENCE_CENTER', 'Neuroscience Center'), ('OBESITY_CENTER', 'Obesity Center'), ('EYE_CENTER', 'Eye Center'), ('ORTHOPEDIC_CENTER', 'Orthopedic Center'), ('PEDIATRIC_CENTER', 'Pediatric Center')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
