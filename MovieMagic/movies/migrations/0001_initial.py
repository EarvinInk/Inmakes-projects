# Generated by Django 4.0.5 on 2022-06-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='poster')),
                ('short_disc', models.CharField(max_length=250)),
                ('long_disc', models.TextField()),
                ('director', models.CharField(max_length=50)),
                ('release_date', models.IntegerField()),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
    ]
