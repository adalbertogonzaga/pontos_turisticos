from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class ComentarioAprovadoViewSet(ModelViewSet):

    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.filter(aprovado=True)
