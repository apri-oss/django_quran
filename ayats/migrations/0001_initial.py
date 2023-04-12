# Generated by Django 4.1.7 on 2023-03-31 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ayat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ayat_data', models.JSONField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('surat_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surats.surat', verbose_name='ID')),
            ],
        ),
    ]