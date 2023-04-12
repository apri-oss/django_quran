from django.db import models

# Create your models here.
class Surat(models.Model):
    surat_name = models.CharField(max_length = 200, blank=False, null=False)
    surat_seq = models.IntegerField(blank=False, null=False)
    surat_text = models.CharField(max_length = 200, blank=False, null=False)
    surat_terjemahan = models.CharField(max_length = 200, blank=False, null=False)
    golongan_surah = models.CharField(max_length = 200, blank=False, null=False)
    jumlah_ayat = models.IntegerField(blank=False, null=False)
    datetime = models.DateTimeField(auto_now=True)