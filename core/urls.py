from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SermonViewSet # We need to create this next!

# This is the "Automated Address Book"
router = DefaultRouter()
router.register(r'sermons', SermonViewSet, basename='sermon')

urlpatterns = router.urls