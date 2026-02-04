from rest_framework import generics
from .models import Topic
from .serializers import TopicListSerializer, TopicDetailSerializer


# 🌍 Public topic list (W3-style sidebar)
class PublicTopicListAPIView(generics.ListAPIView):
    queryset = Topic.objects.filter(is_public=True)
    serializer_class = TopicListSerializer


# 📘 Single topic page with PDFs
class PublicTopicDetailAPIView(generics.RetrieveAPIView):
    queryset = Topic.objects.filter(is_public=True)
    serializer_class = TopicDetailSerializer
    lookup_field = "slug"
