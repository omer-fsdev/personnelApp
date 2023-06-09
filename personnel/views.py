from django.shortcuts import render
from .models import Department, Personnel
from .serializers import (
    DepartmentSerializer,
    PersonnelSerializer,
    DepartmentPersonnelSerializer,
)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsStaffOrReadOnly


# Create your views here.


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class PersonnelView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    permission_classes = [IsAuthenticated]


class PersonnelUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    permission_classes = [IsAuthenticated]


class DepartmentPersonnelView(generics.ListAPIView):
    serializer_class = DepartmentPersonnelSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated]


class Custom(generics.RetrieveAPIView):
    serializer_class = DepartmentPersonnelSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "name"
