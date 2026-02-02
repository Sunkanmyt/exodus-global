from rest_framework import serializers
from .models import Sermon, Event, Milestone, ContactMessage, Partnertier, Partner, MinistryInfo

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class PartnertierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnertier
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    tier_details = PartnertierSerializer(source='tier', read_only=True)
    class Meta:
        model = Partner
        fields = ['id', 'full_name', 'email', 'tier', 'tier_details', 'joined_on', 'is_active']

class MinistryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryInfo
        fields = '__all__'