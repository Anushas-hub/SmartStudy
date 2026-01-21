from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudyMaterial
from .serializers import StudyMaterialSerializer

@api_view(['GET'])
def material_list(request):
    materials = StudyMaterial.objects.all()
    serializer = StudyMaterialSerializer(materials, many=True)
    return Response(serializer.data)
