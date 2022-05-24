from django.shortcuts import render
from .models import Beca
# Create your views here.
def paginaprincipal(request):
    becas = Beca.objects.all().order_by('-Popularidad')[:5]
    contexto = {
        'bequitas': becas
    }
    return render(request,'index.html',contexto)

def AumentarYVer(request,id):
    beca = Beca.objects.get(id=id)
    beca.Popularidad = beca.Popularidad + 1
    beca.save()