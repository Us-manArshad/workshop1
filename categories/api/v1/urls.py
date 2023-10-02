from django.urls import include, path
from rest_framework.routers import DefaultRouter

from categories.api.v1.viewsets import CategoryViewSet

router = DefaultRouter()


router.register("category", CategoryViewSet, basename="categories")


urlpatterns = [
    path("", include(router.urls)),
]
