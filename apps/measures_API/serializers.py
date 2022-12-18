from rest_framework import serializers

from .models import Measure


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'device_id', 'measure_value', 'measure_unit', 'measure_date']
