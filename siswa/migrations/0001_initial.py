# Generated by Django 4.1.3 on 2022-12-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NISN', models.CharField(max_length=40)),
                ('tanggal_lahir', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
                ('jenis_kelamin', models.CharField(max_length=40)),
            ],
        ),
    ]
