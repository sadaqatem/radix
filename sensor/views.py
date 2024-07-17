


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorDataSerializer
from django.shortcuts import render

@api_view(['GET', 'POST'])
def sensor_data_view(request):
    if request.method == 'GET':
        return render(request, 'sensor_data_form.html')
    
    elif request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'success.html')
        else:
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['Get','POST'])
def upload_csv_view(request):
    if request.method == 'GET':
        return render(request, 'upload_csv.html')
    csv_file = request.FILES.get('file')
    if not csv_file.name.endswith('.csv'):
        return Response({'error': 'File is not CSV type'}, status=status.HTTP_400_BAD_REQUEST)
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    # Skip header row
    next(io_string)  
    for column in csv.reader(io_string, delimiter=','):
        _, created = SensorData.objects.update_or_create(
            equipment=Equipment.objects.get_or_create(equipment_id=column[0])[0],
            timestamp=column[1],
            value=column[2]
        )
        return render(request, 'success.html')
    
    return render(request,'upload_csv.html')





@api_view(['GET'])
def average_sensor_data_view(request):
    period = request.query_params.get('period', '24h')
    time_delta = timedelta(hours=24)
    
    if period == '48h':
        time_delta = timedelta(hours=48)
    elif period == '1w':
        time_delta = timedelta(weeks=1)
    elif period == '1m':
        time_delta = timedelta(days=30)
    
    end_time = parse_datetime(request.query_params.get('end_time', str(datetime.now())))
    start_time = end_time - time_delta

    avg_values = SensorData.objects.filter(timestamp__range=(start_time, end_time)).values('equipment__equipment_id').annotate(avg_value=Avg('value'))

    return Response(avg_values)



def register_success(request):
    return render(request, 'success.html')