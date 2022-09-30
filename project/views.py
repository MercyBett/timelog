from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOwnerOrAdminOrReadOnly
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated,IsOwnerOrAdminOrReadOnly]
  serializer_class = ProjectSerializer
  queryset=Project.objects.all()

