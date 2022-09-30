from rest_framework import serializers
from .models import ProjectTracker
from users.models import User
from project.models import Project

class ProjectTrackerSerializer(serializers.ModelSerializer):


  user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False)
  project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), many=False)
  class Meta:
    model = ProjectTracker
    fields = '__all__'


    def validate(self, data):
      if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("finish must occur after start")
      return data