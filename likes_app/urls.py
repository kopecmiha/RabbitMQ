from django.urls import path, include
from .views import QuoteViewSet, QuoteUserViewSet, like
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('quotes', QuoteViewSet, basename='quotes')
router.register('quoteusers', QuoteUserViewSet, basename='quoteusers')

urlpatterns = [
    path('', include(router.urls)),
    path('quotes/<int:pk>/like', like)
]
