from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import Wiki
from .serializers import WikiDetailSerializer


class RetrieveWikiDetailApi(RetrieveAPIView):
    queryset = Wiki.objects
    serializer_class = WikiDetailSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )
