# Generated by Django 4.1.7 on 2023-03-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surat_name', models.CharField(max_length=200)),
                ('surat_seq', models.IntegerField()),
                ('surat_text', models.CharField(max_length=200)),
                ('surat_terjemahan', models.CharField(max_length=200)),
                ('golongan_surah', models.CharField(max_length=200)),
                ('jumlah_ayat', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
