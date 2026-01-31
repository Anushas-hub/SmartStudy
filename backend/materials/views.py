from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudyMaterial
from .serializers import StudyMaterialSerializer
from .permissions import IsAdminOrAuthor

@api_view(['GET'])
def material_list(request):
    materials = StudyMaterial.objects.all()
    serializer = StudyMaterialSerializer(materials, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminOrAuthor])
def upload_material(request):
    serializer = StudyMaterialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(uploaded_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
