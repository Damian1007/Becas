from django.urls import path
from .import views

urlpatterns = [
    path('',views.paginaprincipal,name="index"),
    path('eliminarBeca/<int:id>', views.eliminarBeca, name="eliminar"),
    path('<int:id>', views.detalleBeca, name="detalleBeca"),  
    
]