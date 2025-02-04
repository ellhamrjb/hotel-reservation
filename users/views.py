from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
   #(Admin only)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
