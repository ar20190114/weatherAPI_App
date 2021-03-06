# Generated by Django 3.1 on 2022-06-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=100)),
                ('temperature', models.IntegerField()),
            ],
            options={
                'verbose_name': '天気情報',
                'verbose_name_plural': '天気情報',
            },
        ),
    ]
