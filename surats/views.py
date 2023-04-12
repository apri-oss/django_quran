from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from surats.models import Surat
from surats.serializers import SuratSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def surat_list(request):

  # create data surat
  if request.method == 'POST':
    surat_data = JSONParser().parse(request)
    surat_list = []
    for value in surat_data['data']: 
      existing_surat_list = Surat.objects.filter(surat_seq = value['id'])
      if existing_surat_list:
        existing_surat_list.delete()


      item ={
        'surat_name': value['arabic'],
        'surat_text' : value['latin'],
        'surat_terjemahan': value['translation'],
        'golongan_surah': value['location'],
        'surat_seq': value['id'],
        'jumlah_ayat': value['num_ayah']
      }
      surat_list.append(item)
    surat_serializer = SuratSerializer(data=surat_list, many=True)
    if surat_serializer.is_valid():
      surat_serializer.save()
      return JsonResponse(surat_serializer.data,  safe=False, status=status.HTTP_201_CREATED) 
    return JsonResponse(surat_serializer.errors,  safe=False, status=status.HTTP_400_BAD_REQUEST)
  

  # get data surat
  if request.method == 'GET':
    surats = Surat.objects.all()    
    # filtering data by surat_text
    filter_surat_name = request.GET.get('surat_text', None)
    if filter_surat_name is not None:
      surats = surats.filter(surat_text__icontains=filter_surat_name)

    surat_serializer = SuratSerializer(surats, many=True)
    return JsonResponse(surat_serializer.data, safe=False)