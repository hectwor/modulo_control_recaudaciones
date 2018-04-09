from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()


urlpatterns = [
    url(r'^hello/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]