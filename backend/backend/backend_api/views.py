from rest_framework import generics
from backend1.models import data
from .serializers import dataSerializer

# Create your views here.

class dataList(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerializer
  


class dataDetail(generics.RetrieveDestroyAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerializer
