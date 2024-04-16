from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from . import serializers
from . import models

class DepartmentView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        departments = models.DepartmentModel.objects.all()
        serializer = serializers.DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentScheduleView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, department_id, format=None):
        department = models.DepartmentModel.objects.get(id=department_id)
        axis_data = models.AxisModel.objects.filter(department=department)
        schedule_data = models.ScheduleModel.objects.filter(department=department)
        return Response(
            {
                "department": serializers.DepartmentSerializer(department).data,
                "axis": serializers.AxisSerializer(axis_data, many=True).data,
                "schedule": serializers.ScheduleSerializer(
                    schedule_data, many=True
                ).data,
            }
        )


class AxisView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = serializers.AxisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = serializers.ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDeleteView(APIView):
    # permission_classes = [IsAuthenticated]

    def delete(self, request, schedule_id, format=None):
        try:
            schedule = models.ScheduleModel.objects.get(id=schedule_id)
            schedule.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.ScheduleModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
