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
