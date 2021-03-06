# Generated by Django 4.0.3 on 2022-04-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_detailed_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='passaeger_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trip_same_id', models.IntegerField(default=1)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=10)),
                ('username', models.CharField(max_length=10)),
                ('Trip_date', models.DateField()),
                ('payment', models.IntegerField(default=50)),
                ('city', models.CharField(max_length=20)),
                ('pay_done', models.IntegerField(default=0)),
            ],
        ),
    ]
