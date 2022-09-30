
from .views import ProjectViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('projects',ProjectViewSet,basename="projects")

urlpatterns=router.urls

