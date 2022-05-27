from .views import Beca
from django.forms import ModelForm

class BecaForm(ModelForm):
    class Meta:
        model = Beca
        fields = '__all__'