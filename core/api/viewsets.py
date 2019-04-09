from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        print('overriden list')
        return ModelViewSet.list(self,request,*args, **kwargs)

    def create(self, request, *args, **kwargs):
        print('overriden create')
        return ModelViewSet.create(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print('overriden destroy')
        return Response({'response': 'Could not Delete', 'error_code': 403})
        # return ModelViewSet.destroy(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('overriden retrieve')
        return ModelViewSet.retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print('overriden update')
        return ModelViewSet.update(self, request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print('overriden partial_update')
        return ModelViewSet.partial_update(self, request, *args, **kwargs)

    @action(methods=['post'], detail=True)  # Example: http://127.0.0.1:8000/api/pontosturisticos/5/denunciar/
    def denunciar(self, request, pk=None):
        print('action denunciar')
        return Response({'response': f'The id:{pk} entry was reported', 'response_code': 201})

    @action(methods=['get'], detail=False)  # Example: http://127.0.0.1:8000/api/pontosturisticos/teste_get_last/
    def teste_get_last(self, request):
        print('action teste_get_last')
        serializer = PontoTuristicoSerializer(PontoTuristico.objects.all().last())
        return Response( {'last_object': serializer.data}, 200)
        # return Response({'response': f'The "teste action" has been hit', 'response_code': 201})
