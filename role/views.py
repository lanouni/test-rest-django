from django.shortcuts import render
from rest_framework import generics, status
from .models import Role
from .serializers import *
from rest_framework.response import Response


class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleCreate(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePostSerializer

class RoleUpdate(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePostSerializer

    def put(self, request, *args, **kwargs):
        name = request.data.get('name')
        role = Role.objects.get()
        if not role:
            return Response({'message': 'Role does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if name != role.name:
            return Response({'message': 'You can only update name'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Role updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)