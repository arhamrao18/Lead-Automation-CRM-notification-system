from rest_framework import serializers
from.models import Lead

class LeadSerializer(serializers.Serializer):
    class meta:
        model = Lead
        fields = '__all__'
