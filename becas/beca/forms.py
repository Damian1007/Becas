from .views import Beca
from django.forms import ModelForm

class BecaForm(ModelForm):
    class Meta:
        model = Beca
        fields = ['Nombre', 'Categoria', 'Porcentaje_F' ,'Pais' ,'Universidad' ,'Requirimientos', 'Popularidad']