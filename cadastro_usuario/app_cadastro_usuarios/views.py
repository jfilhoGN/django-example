from django.shortcuts import render
from app_cadastro_usuarios.models import Cliente
# Create your views here.
def index(request):
    lista = Cliente.objects.all()
    context = {
        'lista': lista
    }
    return render(request, 'index.html', context)