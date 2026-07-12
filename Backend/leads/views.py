from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Lead
from .serializers import LeadSerializer


class LeadCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

'''It will check that message is already present'''

class LeadCheckView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        phone = request.query_params.get("phone")
        if not phone:
            return Response({"error": "phone parameter required"}, status=400)

        lead = Lead.objects.filter(phone=phone).first()
        if lead:
            return Response(LeadSerializer(lead).data, status=200)
        return Response({"exists": False}, status=404)


'''If present then it will change the status like submission date'''

class LeadUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer