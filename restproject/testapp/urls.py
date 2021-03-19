from django.urls import path,include
from testapp import views
from .views import ArticleAPIView,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('article/', views.article_list),
    path('classarticle/', ArticleAPIView.as_view()),
    path('generic/', GenericAPIView.as_view()),
    path('detail/<int:id>', views.article_detail),
]
