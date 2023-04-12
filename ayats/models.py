from django.db import models
from surats.models import Surat


# Create your models here.
class Ayat(models.Model):
  surat_id = models.ForeignKey(Surat, verbose_name="ID", on_delete=models.PROTECT)
  ayat_data = models.JSONField()
  datetime = models.DateTimeField(auto_now=True)
  