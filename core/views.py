from rest_framework import viewsets, permissions
from .models import Sermon, Event, Milestone, ContactMessage, MinistryInfo, Partnertier, Partner
from .serializers import (SermonSerializer, EventSerializer, MilestoneSerializer, ContactMessageSerializer, MinistryInfoSerializer, PartnertierSerializer, PartnerSerializer)

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date_preached')
    serializer_class = SermonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_date')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset =  Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        return super().get_permissions()

class PartnertierViewSet(viewsets.ModelViewSet):
    queryset = Partnertier.objects.all()
    serializer_class = PartnertierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MinistryInfoViewSet(viewsets.ModelViewSet):
    queryset = MinistryInfo.objects.all()
    serializer_class = MinistryInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]