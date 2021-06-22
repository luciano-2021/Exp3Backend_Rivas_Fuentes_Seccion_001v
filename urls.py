from django.urls import path
from .views import home, galeriadefotos, recetario

# llamar a los metodos del veiws.py


urlpatterns = [
    path('', home, name="home"),
    path('galeriadefotos', galeriadefotos, name="galeriadefotos"),
    path('recetario', recetario, name="recetario"),
]

