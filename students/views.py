from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def student_home(request):
    return Response({
        "message": "Welcome to the Student API"
    })

# Create your views here.
