# Generated by Django 4.0.3 on 2022-04-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_passaeger_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passaeger_detail',
            name='Trip_date',
            field=models.DateField(null=True),
        ),
    ]
