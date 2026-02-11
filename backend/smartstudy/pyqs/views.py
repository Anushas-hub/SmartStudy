from rest_framework.generics import ListAPIView
from .models import PYQ
from .serializers import PYQSerializer


class PYQListView(ListAPIView):
    queryset = PYQ.objects.all().order_by("-year")
    serializer_class = PYQSerializer
