from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('mypage.html')
  return HttpResponse(template.render())