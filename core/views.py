from rest_framework import viewsets
from .models import Sermon, Event, Milestone, ContactMessage, MinistryInfo
from .serializers import (SermonSerializer, EventSerializer, MilestoneSerializer, ContactMessageSerializer, MinistryInfoSerializer)

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date_preached')
    serializer_class = SermonSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_date')
    serializer_class = EventSerializer

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset =  Milestone.objects.all()
    serializer_class = MilestoneSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class MinistryInfoViewSet(viewsets.ModelViewSet):
    queryset = MinistryInfo.objects.all()
    serializer_class = MinistryInfoSerializer