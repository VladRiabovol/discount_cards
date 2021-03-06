# Generated by Django 3.2.3 on 2021-12-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('end_of_activity', models.DateField()),
                ('date_of_use', models.DateTimeField(auto_now=True)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
