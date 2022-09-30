from django.urls import path,include
from .views import RegisterView, RetrieveView, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register', RegisterView.as_view()),
    path('retrieve', RetrieveView.as_view(),name="user-list"),
]
