from django.shortcuts import render
from django.http import HttpResponse

from apps.contato.models import Contato

def index(requisicao):

   dados = Contato.objects.all()
   return render (requisicao,'index.html', {'contatos':dados})

   
def form (requisicao):
    return render (requisicao, 'form.html')
