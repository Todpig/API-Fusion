from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from Core.views import FuncionarioViewSet, ServicosViewSet, ProdutosViewSet, SaldoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/refresh', TokenRefreshView.as_view()),
    path('', include('Core.urls')),
    path('serializer/', include("Core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Fusion'
admin.site.site_title = 'Fusion'
admin.site.index_title = 'Gerenciamento'
