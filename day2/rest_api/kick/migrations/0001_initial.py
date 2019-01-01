# Generated by Django 2.0.4 on 2019-01-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KickstarterTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backers_count', models.IntegerField()),
                ('blurb', models.TextField()),
                ('category', models.TextField()),
                ('converted_pledged_amount', models.IntegerField()),
                ('country', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('creator', models.TextField()),
                ('currency', models.TextField()),
                ('currency_symbol', models.TextField()),
                ('currency_trailing_code', models.TextField()),
                ('current_currency', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('disable_communication', models.BooleanField()),
                ('friends', models.TextField()),
                ('fx_rate', models.FloatField()),
                ('goal', models.FloatField()),
                ('kickstarter_id', models.IntegerField()),
                ('is_backing', models.TextField()),
                ('is_starrable', models.BooleanField()),
                ('is_starred', models.TextField()),
                ('launched_at', models.DateTimeField()),
                ('location', models.TextField()),
                ('name', models.TextField()),
                ('permissions', models.TextField()),
                ('photo', models.TextField()),
                ('pledged', models.FloatField()),
                ('profile', models.TextField()),
                ('slug', models.TextField()),
                ('source_url', models.URLField()),
                ('spotlight', models.BooleanField()),
                ('staff_pick', models.BooleanField()),
                ('state', models.TextField()),
                ('state_changed_at', models.DateTimeField()),
                ('static_usd_rate', models.FloatField()),
                ('urls', models.TextField()),
                ('usd_pledged', models.FloatField()),
                ('usd_type', models.TextField()),
            ],
        ),
    ]
