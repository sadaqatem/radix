from django import forms
from .models import Equipment, SensorData

class SensorDataForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = '__all__'
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }