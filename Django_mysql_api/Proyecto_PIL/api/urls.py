from django.urls import path
from .views import NotaView

urlpatterns = [
    path('notas/', NotaView.as_view(), name='notas_list'),
    path('notas/<int:id>', NotaView.as_view(), name='notas_process')
]