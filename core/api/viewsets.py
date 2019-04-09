from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    #  Example: http://127.0.0.1:8000/api/pontosturisticos/?search=<search_parameter>
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        print('overriden list')
        return super(PontoTuristicoViewSet, self).list(request,*args, **kwargs)

    def create(self, request, *args, **kwargs):
        print('overriden create')
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print('overriden destroy')
        return Response({'response': 'Could not Delete', 'error_code': 403})

    def retrieve(self, request, *args, **kwargs):
        print('overriden retrieve')
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print('overriden update')
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print('overriden partial_update')
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post'], detail=True)  # Example: http://127.0.0.1:8000/api/pontosturisticos/5/denunciar/
    def denunciar(self, request, pk=None):
        print('action denunciar')
        return Response({'response': f'The id:{pk} entry was reported', 'response_code': 201})

    @action(methods=['get'], detail=False)  # Example: http://127.0.0.1:8000/api/pontosturisticos/teste_get_last/
    def teste_get_last(self, request):
        print('action teste_get_last')
        serializer = PontoTuristicoSerializer(PontoTuristico.objects.all().last())
        return Response( {'last_object': serializer.data}, 200)
