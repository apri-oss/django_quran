from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surat_name', models.CharField(max_length = 200, blank=False, null=False)),
                ('surat_text', models.CharField(max_length = 200, blank=False, null=False)),
                ('surat_terjemahan', models.CharField(max_length = 200, blank=False, null=False)),
                ('golongan_surah', models.CharField(max_length = 200, blank=False, null=False)),
                ('surat_seq', models.IntegerField(blank=False, null=False)),
                ('jumlah_ayat', models.IntegerField(blank=False, null=False)),
                ('datetime', models.DateTimeField(auto_now=True)),


            ],
        ),
    ]