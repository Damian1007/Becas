from django.urls import path
from .import views

urlpatterns = [
    path('',views.paginaprincipal,name="index"),
    path('agregarBeca/', views.agregarBeca, name = "agregar"),
    path('eliminarBeca/<int:id>', views.eliminarBeca, name="eliminar"),
    path('<int:id>', views.detalleBeca, name="detalleBeca"),  
    path('editarbeca/<int:id>', views.editarbecaget,name="editarbeca"),
    path('editarbecaput/<int:id>',views.editarbecaput,name="registrarbeca"),
    path('salir/', views.salir, name="salir")
]