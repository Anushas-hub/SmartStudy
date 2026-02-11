from rest_framework import generics
from .models import PreviousYearQuestion
from .serializers import PreviousYearQuestionSerializer

class PYQListView(generics.ListAPIView):
    queryset = PreviousYearQuestion.objects.all()
    serializer_class = PreviousYearQuestionSerializer
