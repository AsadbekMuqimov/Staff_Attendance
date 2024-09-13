from main import models 
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone


from rest_framework import viewsets
from main.models import Staff, StaffAttendance, Position, Shift, StaffShift
from .serializers import StaffSerializer, StaffAttendanceSerializer, PositionSerializer, ShiftSerializer, StaffShiftSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class StaffShiftViewSet(viewsets.ModelViewSet):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer

@api_view(['GET'])
def staff_list(request):
    """For staff list"""
    staff=models.Staff.objects.all()
    serializer_date = serializers.StaffSerializerList(staff, many=True)

    return Response(serializer_date.data)


@api_view(['POST'])
def staffattendance_create(request):
    """create reports"""
    serializer_data = serializers.StaffAttendanceSerializer(data=request.data)
    if serializer_data.is_valid():
        staff = serializer_data.validated_data.get('staff')
        start_time = serializer_data.validated_data.get('start_time')
        end_time = serializer_data.validated_data.get('end_time')

        if not start_time:
            start_time = timezone.now()
            serializer_data.validated_data['start_time'] = start_time

        last_attendance = models.StaffAttendance.objects.filter(staff=staff).last()

        if last_attendance and not end_time:
            last_attendance.end_time = start_time
            last_attendance.save()
        else:
            serializer_data.save()

        return Response({'success': True})
    return Response({'success': False})

@api_view(['GET'])
def position_list(request):
    position=models.Position.objects.all()
    serializer_date = serializers.PositionSerializerList(position, many=True)
    
    return Response(serializer_date.data)

@api_view(['GET'])
def shift_list(request):
    shift=models.Shift.objects.all()
    serializer_date = serializers.ShiftSerializerList(shift, many=True)
    
    return Response(serializer_date.data)