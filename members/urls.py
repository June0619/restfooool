from django.urls import path, include
from rest_framework import routers

from members import views
from members.views import *

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]