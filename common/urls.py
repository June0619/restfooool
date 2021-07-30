from django.urls import path

from common.views import hello_rest_fooool

urlpatterns = [
    path("hello/", hello_rest_fooool),
]