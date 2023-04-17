
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.template import loader


@api_view(['GET', 'POST', 'DELETE'])
def home(request):
  # return HttpResponse("Hello World!")

  # return render(request, "homepages/templates/home.html")

  template = loader.get_template('index.html')
  return HttpResponse(template.render())

 
