from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponseRedirect

# Create your views here.
from django.forms import ModelForm
from .models import Times

class Times(ModelForm):
  class Meta:
    model = Times
    fields = ['nome_time', 'numero_integrantes', 'inicio_projeto']
    
def index_times(request):
  if request.method == "POST":
      form = Times(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect("/thanks/")
  else:
      form = Times()

  return render(request, "index2.html", {"form": form})