from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartmentModel
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        department, created = models.DepartmentModel.objects.get_or_create(
            name=validated_data["name"]
        )
        return department


class AxisSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    static = serializers.BooleanField(default=True)
    moved = serializers.BooleanField(default=False)

    class Meta:
        model = models.AxisModel
        fields = (
            "id",
            "department",
            "x",
            "y",
            "width",
            "height",
            "name",
            "static",
            "moved",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        department_data = validated_data.pop("department")
        department, created = models.DepartmentModel.objects.get_or_create(
            name=department_data["name"]
        )
        axis, created = models.AxisModel.objects.get_or_create(
            department=department,
            x=validated_data["x"],
            y=validated_data["y"],
            width=validated_data["width"],
            height=validated_data["height"],
            name=validated_data["name"],
            static=validated_data["static"],
            moved=validated_data["moved"],
        )
        return axis


class ScheduleSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    static = serializers.BooleanField(default=False)
    moved = serializers.BooleanField(default=False)

    class Meta:
        model = models.ScheduleModel
        fields = (
            "id",
            "department",
            "x",
            "y",
            "width",
            "height",
            "name",
            "static",
            "moved",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        department_data = validated_data.pop("department")
        department, created = models.DepartmentModel.objects.get_or_create(
            name=department_data["name"]
        )
        schedule, created = models.ScheduleModel.objects.get_or_create(
            department=department,
            x=validated_data["x"],
            y=validated_data["y"],
            width=validated_data["width"],
            height=validated_data["height"],
            name=validated_data["name"],
            static=validated_data["static"],
            moved=validated_data["moved"],
        )
        return schedule
