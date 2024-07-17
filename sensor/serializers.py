from rest_framework import serializers
from .models import SensorData, Equipment

class SensorDataSerializer(serializers.ModelSerializer):
    equipment_id = serializers.CharField(source='equipment.equipment_id')

    class Meta:
        model = SensorData
        fields = ['equipment_id', 'timestamp', 'value']

    def create(self, validated_data):
        equipment_id = validated_data['equipment']['equipment_id']
        equipment, created = Equipment.objects.get_or_create(equipment_id=equipment_id)
        validated_data['equipment'] = equipment
        return super().create(validated_data)