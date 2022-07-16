from rest_framework import generics
from .models import Member
from .serializers import MemeberSerializer

#List View
class ListMembersView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemeberSerializer



