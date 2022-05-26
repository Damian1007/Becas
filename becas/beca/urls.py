from django.urls import path
from .import views

urlpatterns = [
    path('',views.paginaprincipal,name="index"),
    path('AumentarPopularidad/<id>',views.AumentarYVer),
    path('eliminarBeca/<int:id>', views.eliminarBeca, name="eliminar"),
    path('<int:id>', views.detalleBeca, name="detalleBeca"),  
    
]