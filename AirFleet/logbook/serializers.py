from django.db.models import fields
from rest_framework import serializers
from .models import entry

class LogbookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = entry
        fields = [
            'id',
            'pilot_name',
            'flight_date',
            'aircraft_icao',
            'aircraft_reg',
            'from_dest',
            'to_dest',
        ]

class LogbookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = entry
        fields = [
            'id',
            'pilot_name',
            'pilot_identifier',
            'copilot_name',
            'rental_company',
            'airline',
            'flight_date',
            'manufacturer',
            'aircraft_model',
            'aircraft_icao',
            'aircraft_reg',
            'flight_number',
            'from_dest',
            'to_dest',
            'duration',
            'category_and_class',
            'remarks_and_endorsements',
            'picture_with_plane'
        ]