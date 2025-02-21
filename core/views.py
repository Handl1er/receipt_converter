from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import Receipt
from .serializers import ReceiptSerializer
from rest_framework.permissions import IsAuthenticated

class UploadReceiptView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file', None)

        if not file:
            return Response({"error": "Файл не загружен!"}, status=400)

        receipt = Receipt.objects.create(user=request.user, image=file, status='pending')
        return Response({"message": "Чек загружен", "id": receipt.id})
