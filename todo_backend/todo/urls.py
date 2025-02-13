# Import the necessary modules from Django and Django REST framework
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

# Create a router object
router = DefaultRouter()

# Register the viewset with the router
# 'todos' is the URL prefix for this viewset
router.register('todos', TodoViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the URLs provided by the router
    path('', include(router.urls))
]
