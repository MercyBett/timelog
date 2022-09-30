from django.urls import path
from .views import ProjectTrackerViewset
from rest_framework import routers



router = routers.DefaultRouter()

router.register('projectTrackers',ProjectTrackerViewset,basename="projectTrackers")

urlpatterns=router.urls