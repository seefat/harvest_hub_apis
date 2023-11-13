from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    #jwt token generator
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Core Private
    path("api/v1/me", include("core.rest.urls.me")),
    path("api/v1/crops", include("crops.rest.urls.crops")),
    path("api-auth/", include("rest_framework.urls")),
]
