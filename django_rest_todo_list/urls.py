from decouple import config

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=config("API_TITLE"),
        default_version=config("API_VERSION"),
        description=config("API_DESCRIPTION"),
        terms_of_service=config("API_TERMS_OF_SERVICE"),
        contact=openapi.Contact(email=config("API_CONTACT_EMAIL")),
        license=openapi.License(name=config("API_LICENSE")),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path('user/', include('user_profile.urls')),
    path('task/', include('task.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
