from rest_framework.routers import DefaultRouter
from noticia.views import NoticiaViewSet, CategoriaViewSet, LoginView
from django.urls import path

router = DefaultRouter()

router.register(r'noticia', NoticiaViewSet)
router.register(r'categoria', CategoriaViewSet)

urlpatterns = router.urls + [
    path('login/', LoginView.as_view())
]