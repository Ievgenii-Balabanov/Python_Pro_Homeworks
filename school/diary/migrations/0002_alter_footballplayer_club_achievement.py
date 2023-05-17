# Generated by Django 4.2.1 on 2023-05-16 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballplayer',
            name='club',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.CharField(max_length=100)),
                ('achievement', models.CharField(max_length=250)),
                ('football_player_achievements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.footballplayer')),
            ],
        ),
    ]
