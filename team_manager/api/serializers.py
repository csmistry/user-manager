from rest_framework import serializers
from .models import Member

#Serializer for the Member model
class MemeberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'role', 'created_at', 'updated_at')