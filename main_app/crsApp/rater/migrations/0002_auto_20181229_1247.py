# Generated by Django 2.1.4 on 2018-12-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ground_truth_label',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='predicted_label',
            field=models.CharField(max_length=10),
        ),
    ]
