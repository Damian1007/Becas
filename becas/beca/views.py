from django.shortcuts import render
from .models import Beca
import requests
# Create your views here.
def paginaprincipal(request):
    becas = Beca.objects.all().order_by('-Popularidad')[:5]
    response = requests.get("https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=aa53o84KJwAk5rqw9AFhnlw93mAtaRfA")
    dataclean = response.json()
    results = dataclean['results']
    resultsindex = results[:9]
    for i in range(9):    
        try:
            resultsindex[i]['section'] = resultsindex[i]['media'][0]['media-metadata'][2]['url']
        except:
             resultsindex[i]['section'] =  "https://images.unsplash.com/photo-1628155930542-3c7a64e2c833?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974"
        
    fila_n1 = resultsindex[:3]
    fila_n2 = resultsindex[3:6]
    fila_n3 = resultsindex[6:9]
    

    
    contexto = {
        'bequitas': becas,
        'nytimes1': fila_n1,
        'nytimes2': fila_n2,
        'nytimes3': fila_n3,

    }
    return render(request,'index.html',contexto)

def AumentarYVer(request,id):
    beca = Beca.objects.get(id=id)
    beca.Popularidad = beca.Popularidad + 1
    beca.save()