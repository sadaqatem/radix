
from django.urls import path
from .views import sensor_data_view, upload_csv_view, average_sensor_data_view,register_success

urlpatterns = [
    path('sensor-data-view/', sensor_data_view, name='sensor-data-view'),
    path('upload-csv/', upload_csv_view, name='upload-csv-view'),
    path('average-sensor-data/', average_sensor_data_view, name='average-sensor-data-view'),
    path('register/success/', register_success, name='register_success'),

]



