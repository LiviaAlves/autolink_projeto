from rest_framework import routers
from .viewsets import EmpresaViewSet

rota = routers.DefaultRouter()
rota.register(r'empresas', EmpresaViewSet)
