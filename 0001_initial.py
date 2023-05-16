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
                ('position', models.CharField(max_length=5)),
                ('transfer_fee', models.IntegerField()),
                ('club', models.CharField(max_length=2)),
            ],
        ),
    ]
