from django.urls import path , include

# function base API view
from api.views import article_list, article_detail

# class base API view
from api.views import ArticleAPIView, ArticleDetails

# Generics & Mixins
from api.views import GenericAPIView

# Viewset
from api.views import ArticleViewSet

# Using DRF Router for Url/Routing
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename="article")



urlpatterns = [
    # function based API view's url
    # path("article/", article_list),
    # path("article/<int:pk>", article_detail),
    # class based API View url
    path("article/", ArticleAPIView.as_view()),
    path("article/<int:pk>", ArticleDetails.as_view()),
    # Genrics & Mixins
    path("generic/article/", GenericAPIView.as_view()),
    path("generic/article/<int:pk>", GenericAPIView.as_view()),
    
    # viewset
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    
]
