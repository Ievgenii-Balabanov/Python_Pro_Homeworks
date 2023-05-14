# Generated by Django 4.2.1 on 2023-05-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=5, null=True)),
                ('transfer_fee', models.IntegerField(default=0)),
                ('club', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
