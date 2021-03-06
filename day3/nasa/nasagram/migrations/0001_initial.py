# Generated by Django 2.0.4 on 2019-01-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NasaComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('favorite', models.BooleanField()),
                ('comment', models.TextField()),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
    ]
