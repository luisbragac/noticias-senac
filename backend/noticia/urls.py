from rest_framework.routers import DefaultRouter
from noticia.views import NoticiaViewSet

router = DefaultRouter()

router.register(r'noticias', NoticiaViewSet)
urlpatterns = router.urls