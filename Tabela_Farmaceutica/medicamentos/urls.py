from django.urls import path
from .views import lista_medicamentos, novo_medicamento

urlpatterns = [
    path('', lista_medicamentos, name='lista_medicamentos'),
    path('medicamento_form.html/', novo_medicamento, name='add')
]