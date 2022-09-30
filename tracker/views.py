from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOwnerOrAdmin
from .serializers import ProjectTrackerSerializer
from .models import ProjectTracker

class ProjectTrackerViewset(viewsets.ModelViewSet):
  permissions=[IsAuthenticated,IsOwnerOrAdmin]
  serializer_class=ProjectTrackerSerializer

  def get_queryset(self):
    return ProjectTracker.objects.all()