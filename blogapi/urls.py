from django.urls import path, include
app_name = "blogapi"
from .views import *
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views  # Import for token authentication




router = DefaultRouter()
router.register(r'posts', Postview, basename='posts')
router.register(r'comments', Commentview, basename='comments')


# URLs configuration
urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),  # Endpoint for token auth
    path('', include((router.urls))),
]
