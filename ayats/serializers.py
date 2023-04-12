from rest_framework import serializers 
from ayats.models import Ayat
from surats.models import Surat

 
 
class AyatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ayat
    fields = (
      'id',
      'surat_id',
      'ayat_data'
    )


