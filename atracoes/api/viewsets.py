from .serializers import AtracaoSerializer
from atracoes.models import Atracao
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    filter_backends = (DjangoFilterBackend,)  #  http://127.0.0.1:8000/api/atracoes/?nome=<nome>&descricao=<descricao>
    filter_fields = ('nome', 'descricao')
