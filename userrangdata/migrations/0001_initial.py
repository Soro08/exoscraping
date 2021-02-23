# Generated by Django 3.1.7 on 2021-02-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('user_url', models.CharField(blank=True, max_length=255, null=True)),
                ('network', models.CharField(blank=True, max_length=255, null=True)),
                ('last', models.CharField(blank=True, max_length=255, null=True)),
                ('trades', models.CharField(blank=True, max_length=255, null=True)),
                ('total_return', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'UserRank',
                'verbose_name_plural': 'UserRanks',
            },
        ),
    ]