# Generated by Django 2.2.6 on 2021-02-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ingredients', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=1200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('preparation_time', models.DurationField()),
                ('votes', models.SmallIntegerField()),
            ],
        ),
    ]
