# Generated by Django 4.0.4 on 2022-05-05 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('created_dat', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]