from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SermonViewSet, EventViewSet, MilestoneViewSet, ContactMessageViewSet, MinistryInfoViewSet, PartnertierViewSet, PartnerViewSet)

router = DefaultRouter()
router.register(r'sermons', SermonViewSet)
router.register(r'events', EventViewSet)
router.register(r'gallery', MilestoneViewSet)
router.register(r'contact', ContactMessageViewSet)
router.register(r'partner-tiers', PartnertierViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'about', MinistryInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]