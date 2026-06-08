from rest_framework.routers import DefaultRouter
from noticia.views import NoticiaViewSet, CategoriaViewSet

router = DefaultRouter()

router.register(r'noticia', NoticiaViewSet)
router.register(r'categoria', CategoriaViewSet)

urlpatterns = router.urls