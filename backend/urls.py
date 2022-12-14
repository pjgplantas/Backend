"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from media.router import router as media_router
from django.conf import settings
from django.conf.urls.static import static

path("api/media/", include(media_router.urls)),

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)


from pjgplantas.views import (
    BoletoViewSet,
    CartaoViewSet,
    ComentarioViewSet,
    ItensCarrinhoViewSet,
    PedidoViewSet,
    PixViewSet,
    PlantaViewSet,
    RegistrationViewSet,
    MyTokenObtainPairView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register(r"plantas", PlantaViewSet)
router.register(r"boletos", BoletoViewSet)
router.register(r"cartaos", CartaoViewSet)
router.register(r"pixs", PixViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"itens", ItensCarrinhoViewSet)
router.register(r"comentarios", ComentarioViewSet)
router.register(r"auth", RegistrationViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
