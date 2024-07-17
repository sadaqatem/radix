from django.db import models

class Equipment(models.Model):
    equipment_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.equipment_id

class SensorData(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.equipment.equipment_id} - {self.timestamp} - {self.value}'