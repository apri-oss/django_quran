from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from ayats.models import Ayat
from surats.models import Surat
from ayats.serializers import AyatSerializer
from rest_framework.decorators import api_view



@api_view(['GET', 'POST', 'DELETE'])
def detail_ayat(request):

  # create data ayat
  if request.method == 'POST':
    ayat_data = JSONParser().parse(request)
    surat = Surat.objects.filter(surat_seq = ayat_data['number'])
    surat_id = surat.values('id')[0]['id']
    ayat_list = []

    existing_ayat = Ayat.objects.filter(surat_id = surat_id)
    if existing_ayat:
      existing_ayat.delete()

    item ={
      'surat_id': surat_id,
      'ayat_data' : ayat_data['ayahs']
    }
    ayat_list.append(item)

    ayat_serializer = AyatSerializer(data=ayat_list, many=True)
    if ayat_serializer.is_valid():
      ayat_serializer.save()
      return JsonResponse(ayat_list,  safe=False, status=status.HTTP_201_CREATED) 
    return JsonResponse(ayat_list.errors,  safe=False, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_list_ayat(request, pk):
  if request.method == 'GET': 

    response_list=[]
    ayat_list=[]
    surat = Surat.objects.filter(surat_seq=pk)
    # check whether surat exist or not
    if not surat.first() :
      return JsonResponse("DATA NOT FOUND", safe=False) 
    
    surat_id = surat.values('id')[0]['id']
    ayat = Ayat.objects.filter(surat_id=surat_id)
    data_ayats = ayat.values('ayat_data')[0]['ayat_data']

    # convert number to arabic 
    ar_num = '۰١٢٣٤٥٦٧٨٩'
    en_num = '0123456789'
    covertion_table = str.maketrans(en_num, ar_num)
    
    for value in data_ayats :
      arabic_seq = str(value['verseId'])
      surat_seq_arabic = arabic_seq.translate(covertion_table)

      ayat_item={
        "juz":value['juz'],
        "audio":value['audio'],
        "verseId":value['verseId'],
        "arabicVerseId": surat_seq_arabic,
        "ayahText":value['ayahText'],
        "indoText":value['indoText'],
        "readText":value['readText']
      }
      ayat_list.append(ayat_item)



    item ={
      'surat_id': surat_id,
      'surat_seq': surat.values('surat_seq')[0]['surat_seq'],
      'surat_text': surat.values('surat_text')[0]['surat_text'],
      'surat_terjemahan': surat.values('surat_terjemahan')[0]['surat_terjemahan'],
      'golongan_surah': surat.values('golongan_surah')[0]['golongan_surah'],
      'jumlah_ayat': surat.values('jumlah_ayat')[0]['jumlah_ayat'],
      'ayat_data' : ayat_list
    }
    response_list.append(item)

    return JsonResponse(response_list, safe=False) 

