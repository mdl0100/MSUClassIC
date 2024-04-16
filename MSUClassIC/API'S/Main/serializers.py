from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Used to serialize the Department data (name only)
    """

    class Meta:
        model = models.DepartmentModel
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        """
        Create a new department if it does not exist
        Otherwise, get the existing department
        """
        department, created = models.DepartmentModel.objects.get_or_create(
            name=validated_data["name"]
        )
        return department


class AxisSerializer(serializers.ModelSerializer):
    """
    Used to serialize the Axis data
    """

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
        """
        Get the department data from API request
        """
        department_data = validated_data.pop("department")

        """
        Create a new department if it does not exist
        Otherwise, get the existing department
        """
        department, created = models.DepartmentModel.objects.get_or_create(
            name=department_data["name"]
        )

        """
        Create a new axis label if it does not exist
        Otherwise, get the existing axis label
        """
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
    """
    Used to serialize the Schedule data
    """

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
        """
        Get the department data from API request
        """
        department_data = validated_data.pop("department")

        """
        Create a new department if it does not exist
        Otherwise, get the existing department
        """
        department, created = models.DepartmentModel.objects.get_or_create(
            name=department_data["name"]
        )

        """
        Create a new schedule if it does not exist
        Otherwise, get the existing schedule
        """
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
