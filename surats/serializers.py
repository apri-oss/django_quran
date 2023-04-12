from rest_framework import serializers 
from surats.models import Surat
 
 
class SuratSerializer(serializers.ModelSerializer):
  class Meta:
    model = Surat
    fields = (
      'surat_name',
      'surat_text',
      'surat_terjemahan',
      'golongan_surah',
      'surat_seq',
      'jumlah_ayat',
      'datetime'
    )

