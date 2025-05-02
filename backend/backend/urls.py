from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from mecanica.api.router import rota
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from mecanica.views import RegisterView
from mecanica.api.viewsets import ForgotPasswordView, ResetPasswordView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(rota.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh' ),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('api/reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)


