"""
URL configuration for workshop1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("categories.api.v1.urls"))
]

import debug_toolbar


api_info = openapi.Info(
    title="Insurance Admin Panel",
    default_version="v1",
    description="API documentation for Auth Payment",
)
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=[permissions.AllowAny,],
)


urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
