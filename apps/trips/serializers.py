from django.db import transaction
from rest_framework import serializers

from apps.trips.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)

    @transaction.atomic
    def create(self, validated_data):
        trip = Trip.objects.create(
            **validated_data
        )
        return trip

    